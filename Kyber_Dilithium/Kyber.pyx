from .poly.polyvec cimport *
from .poly.polynomial cimport *
from .Kyberutils cimport *
import os
import hashlib

class Kyber:
    def __init__(self ,paramset):
        self.k = paramset["k"]
        self.eta1 = paramset["eta1"]
        self.eta2 = paramset["eta2"]
        self.q = 3329
        self.du = paramset["du"]
        self.dv = paramset["dv"]
    def cpakeygen(self , seed = None):

        # gen seed
        if seed == None:
            seed = os.urandom(32)

        temp = hashlib.sha3_512(seed).digest()
        rho, sigma = temp[:32] , temp[32:]
        
        # sample matrix and vector
        matA = gen_mat(rho , self.k)
        self.A = KyberMat(matA , self.k)
        slist = []
        for i in range(self.k):
            slist.append(CBD(sigma+bytes([i]) , self.eta1))
        self.s = KyberVec(slist , self.k , 0)
        elist = []
        for i in range(self.k):
            elist.append(CBD(sigma+bytes([i+self.k]) , self.eta1))
        e = KyberVec(elist , self.k , 0)
        self.s.to_ntt()
        e.to_ntt()
        self.t = KyberVec(None , self.k , 1)
        self.A.mul(self.t , self.s)
        #self.t.to_poly()
        #print(self.t.getpoly(0))
        #self.t.to_ntt()
        self.t.add(self.t , e)
        # pack pk and sk
        pkarray = self.t.getpoly(1)
        
        pk = pack_vec(pkarray , self.k , 12 , self.q)
        pk += rho
        self.pk = pk
        self.Hpk = hashlib.sha3_256(pk).digest()

        skarray = self.s.getpoly(1)
        sk = pack_vec(skarray , self.k , 12 , self.q)
        return pk , sk
    
    def load_pk(self , pk):
        rho = pk[-32:]
        tbuf = pk[:-32]
        matA = gen_mat(rho , self.k)
        self.A = KyberMat(matA , self.k)

        t = unpack_vec(tbuf , self.k , 12)
        self.t = KyberVec(t , self.k , 1)

        self.pk = pk
        self.Hpk = hashlib.sha3_256(pk).digest()
    def load_sk(self , sk):
        s = unpack_vec(sk , self.k , 12)
        self.s = KyberVec(s , self.k , 1)

        if len(sk) != self.k*32*12:
            sklen = self.k*32*12
            pklen = self.k*32*12+32
            pk = sk[sklen:sklen+pklen]
            self.load_pk(pk)
            self.Hpk = sk[sklen+pklen:sklen+pklen+32]
            self.z = sk[-32:]
    def cpaenc(self , m , rseed):

        # sample
        rlist = []
        for i in range(self.k):
            rlist.append(CBD(rseed+bytes([i]) , self.eta1))
        r = KyberVec(rlist , self.k , 0)

        e1list = []
        for i in range(self.k):
            e1list.append(CBD(rseed+bytes([i+self.k]), self.eta2))
        e1 = KyberVec(e1list , self.k , 0)

        e2list = CBD(rseed+bytes([2*self.k]) , self.eta2)
        e2 = KyberPoly(e2list , 0 ,0)

        # convert m
        mlist = Decode(m , 1)
        mlist = Decompress(self.q , mlist , 1)
        mpoly = KyberPoly(mlist , 0 ,0)

        # enc
        u = KyberVec(None , self.k , 1)
        r.to_ntt()
        self.A.trans()
        self.A.mul(u , r)
        u.to_poly()
        u.add(u , e1)
        
        v = KyberPoly(None , 1 , 1)
        self.t.mul(v , r)
        v.to_poly()
        v.add(v , e2)
        v.add(v , mpoly)
        # pack cipher
        c1list = [Compress(self.q , i , self.du) for i in u.getpoly(0)]
        c1 = pack_vec(c1list , self.k , self.du , 0)
        c2 = Compress(self.q , v._core.polyarray , self.dv)
        c2 = Encode(c2 , self.dv)
        
        return c1 + c2

    def cpadec(self , c):

        # unpack c
        c1len = self.du*32
        c2len = self.dv*32
        c1 , c2 = c[:-c2len] , c[-c2len:]

        # load c
        ulist = unpack_vec(c1 , self.k , self.du)
        ulist = [Decompress(self.q , ulist[i] , self.du) for i in range(self.k)]
        u = KyberVec(ulist ,self.k, 0)

        vlist = Decode(c2 , self.dv)
        vlist = Decompress(self.q , vlist , self.dv)
        v = KyberPoly(vlist , 0, 0)
        
        # recover m
        mpoly = KyberPoly(None , 1 , 1)
        u.to_ntt()
        self.s.mul(mpoly , u)
        mpoly.to_poly()
        v.sub(mpoly , mpoly)
        m = Compress(self.q , mpoly._core.polyarray , 1)
        m = Encode(m , 1)
        return m
    
    def keygen(self):
        z = os.urandom(32)
        pk ,sk1 = self.cpakeygen()
        sk = sk1 + pk + hashlib.sha3_256(pk).digest() + z
        self.load_sk(sk)
        return pk , sk
    
    def kemenc(self , Klen = 128):
        m = os.urandom(32)
        m = hashlib.sha3_256(m).digest()
        temp = hashlib.sha3_512(m + self.Hpk).digest()
        _K , r = temp[:32] , temp[32:]
        c = self.cpaenc(m , r)
        K = hashlib.shake_256(_K + hashlib.sha3_256(c).digest()).digest(Klen//8)
        return c , K
    
    def kemdec(self, c, Klen = 128):
        _m = self.cpadec(c)
        temp = hashlib.sha3_512(_m + self.Hpk).digest()
        __K , _r = temp[:32] , temp[32:]
        _c = self.cpaenc(_m , _r)
        if _c == c:
            K = hashlib.shake_256(__K + hashlib.sha3_256(c).digest()).digest(Klen//8)
        else:
            K = hashlib.shake_256(self.z + hashlib.sha3_256(c).digest()).digest(Klen//8)
        return K