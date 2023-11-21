import os
import hashlib
from .Dilithiumutils cimport *
from .poly.polyvec cimport *
from .poly.polynomial cimport *

class Dilithium:
    def __init__(self ,paramset):
        self.k = paramset["k"]
        self.eta = paramset["eta"]
        self.l = paramset["l"]
        self.q = 8380417
        self.d = paramset["d"]
        self.loggamma1 = paramset["loggamma1"]
        self.gamma2 = paramset["gamma2"]
        self.tau = paramset["tau"]
        self.beta = self.tau * self.eta
        self.omega = paramset["omega"]
    def keygen(self):
        # generate seed
        zeta = os.urandom(32)
        temp = hashlib.shake_256(zeta).digest(96)
        rho , rhoprime , K = temp[:32] , temp[32:64] , temp[64:]
        self.K = K
        # sample vector
        slist = rej_eta(self.eta , rhoprime , self.l + self.k)
        s1 = slist[:self.l]
        s2 = slist[self.l:]
        self.s1 = DilithiumVec(s1 , self.l , 0)
        self.s2 = DilithiumVec(s2 , self.k , 0)
        
        A = ExpandA(rho , self.k ,self.l)
        self.A = DilithiumMat(A , self.k , self.l)
        
        # compute pubkey
        self.t = DilithiumVec(None , self.k , 1)
        self.s1.to_ntt()
        self.A.mul(self.t , self.s1)
        self.t.to_poly()
        self.t.add(self.t , self.s2)

        # compute t
        t1 = []
        t0 = []
        temp = self.t.getpoly(0)
        for i in range(self.k):
            temp1 ,temp2 = Power2Round(temp[i] , self.d)
            t1.append(temp1)
            t0.append(temp2)
        # pack pk
        packed_t1 = pack_vec(t1 ,self.k , 23 - self.d , 0)
        pk = rho + packed_t1

        # pack sk
        self.tr = hashlib.shake_256(pk).digest(48)
        etabit = len(bin(self.eta)) - 2
        packed_s1 = pack_vec(s1 , self.l , etabit , 1)
        packed_s2 = pack_vec(s2 , self.k , etabit , 1)
        packed_t0 = pack_vec(t0 , self.k , self.d , 1)
        sk = rho + K + self.tr + packed_s1 + packed_s2 + packed_t0

        # load pk
        for i in range(self.k):
            for j in range(256):
                t1[i][j] *= 2**self.d
        self.t1 = DilithiumVec(t1 , self.k , 0)
        self.t1.to_ntt()

        # load sk
        self.t0 = DilithiumVec(t0 , self.k , 0)
        self.s2.to_ntt()
        self.t0.to_ntt()

        return pk ,sk

    def load_pk(self , pk):
        rho = pk[:32]
        packed_t1 = pk[32:]
        self.tr = hashlib.shake_256(pk).digest(48)
        
        # load A
        A = ExpandA(rho , self.k ,self.l)
        self.A = DilithiumMat(A , self.k , self.l)

        # load t1
        t1 = unpack_vec(packed_t1 , self.k , 23 - self.d , 0)
        for i in range(self.k):
            for j in range(256):
                t1[i][j] *= 2**self.d
        
        self.t1 = DilithiumVec(t1 , self.k , 0)
        self.t1.to_ntt()

    def load_sk(self , sk):
        rho = sk[:32]
        self.K = sk[32:64]
        self.tr = sk[64:112]
        etabit = len(bin(self.eta)) - 2
        s1len = (etabit + 1) * 32 * self.l
        s2len = (etabit + 1) * 32 * self.k
        t0len = (self.d + 1) * 32 * self.k

        # load A
        A = ExpandA(rho , self.k ,self.l)
        self.A = DilithiumMat(A , self.k , self.l)

        # load s1,s2,t0
        packed_s1 = sk[112:112+s1len]
        packed_s2 = sk[112+s1len:112+s1len+s2len]
        packed_t0 = sk[-t0len:]

        s1 = unpack_vec(packed_s1 , self.l , etabit , 1)
        s2 = unpack_vec(packed_s2 , self.k , etabit , 1)
        t0 = unpack_vec(packed_t0 , self.k , self.d , 1)
        
        self.s1 = DilithiumVec(s1 , self.l , 0)
        self.s2 = DilithiumVec(s2 , self.k , 0)
        self.t0 = DilithiumVec(t0 , self.k , 0)
        self.s1.to_ntt()
        self.s2.to_ntt()
        self.t0.to_ntt()
    def sign(self , m):
        mu = hashlib.shake_256(self.tr + m).digest(384)
        kapa, z ,h = 0 , None , None
        _rho = hashlib.shake_256(self.K + mu).digest(384)
        while (z == None or h == None):
            # compute w
            ylist = ExpandMask(_rho , kapa , self.l , self.loggamma1)
            y = DilithiumVec(ylist , self.l , 0)
            y.to_ntt()
            w = DilithiumVec(None , self.k , 1)
            self.A.mul(w , y)
            w.to_poly()

            wlist = w.getpoly(0)
            w1 = []
            for i in range(self.k):
                w1.append(HighBits(wlist[i] , 2*self.gamma2))
            # get c
            packed_w1 = pack_vec(w1 , self.k , 23 - self.gamma2.bit_length() , 0)
            _c = hashlib.shake_256(mu + packed_w1).digest(32)
            clist = SampleInBall(_c , self.tau)
            
            # compute z
            c = DilithiumPoly(clist , 0 , 0)
            c.to_ntt()
            z = DilithiumVec(None , self.l , 1)
            self.s1.polymul(z , c)
            z.add(z , y)
            z.to_poly()

            # compute r0
            r0poly = DilithiumVec(None , self.k , 1)
            self.s2.polymul(r0poly , c)
            r0poly.to_poly()
            w.sub(r0poly , r0poly)
            r0list = r0poly.getpoly(0)
            r0 = []
            for i in range(self.k):
                r0.append(LowBits(r0list[i] , 2*self.gamma2))

            # judge
            if (inf_norm(z.getpoly(0)) >= (1<<self.loggamma1) - self.beta) or (inf_norm(r0) >= self.gamma2-self.beta):
                z = None
                kapa = kapa + self.l
                continue

            # make hint
            # ct0
            ct0 = DilithiumVec(None ,self.k,1)
            self.t0.polymul(ct0 , c)
            ct0.to_poly()
            if inf_norm(ct0.getpoly(0)) >= self.gamma2:
                z = None
                kapa = kapa + self.l
                continue
            ct0.add(ct0 , r0poly)
            h,cnt = MakeHint(r0list , ct0.getpoly(0) , 2*self.gamma2)
            if cnt > self.omega:
                z = None
                h = None
                kapa = kapa + self.l
                continue
            
            # pack signature
            packed_z = pack_vec(z.getpoly(0) , self.l, self.loggamma1 , 1)
            packed_h = pack_vec(h , self.k , 1 , 0)
            sign = packed_z + packed_h + _c
        return sign
    def verify(self , m , sign):
        # unpack signature
        mu = hashlib.shake_256(self.tr + m).digest(384)
        zlen = (self.loggamma1+1)*self.l*32
        hlen = self.k * 32
        packed_z = sign[:zlen]
        packed_h = sign[zlen:hlen+zlen]
        _c = sign[-32:]
        zlist = unpack_vec(packed_z , self.l , self.loggamma1 , 1)
        hlist = unpack_vec(packed_h , self.k , 1 , 0)
        z = DilithiumVec(zlist , self.l , 0)
        clist = SampleInBall(_c , self.tau)
        c = DilithiumPoly(clist , 0 , 0)

        # check inf_norm(z)
        if (inf_norm(zlist) >= (1<<self.loggamma1) - self.beta):
            return False
        # check h's 1
        if cnt_one(hlist) > self.omega:
            return False

        # compute w
        z.to_ntt()
        c.to_ntt()
        w = DilithiumVec(None , self.k , 1)
        self.A.mul(w , z)
        temp = DilithiumVec(None , self.k, 1)
        self.t1.polymul(temp , c)
        w.sub(w , temp)
        w.to_poly()
        _w1 = UseHint(hlist , w.getpoly(0) , 2*self.gamma2)
        # check _c
        packed_w1 = pack_vec(_w1 , self.k , 23 - self.gamma2.bit_length() , 0)
        __c = hashlib.shake_256(mu + packed_w1).digest(32)
        if _c == __c:
            return True
        return False




