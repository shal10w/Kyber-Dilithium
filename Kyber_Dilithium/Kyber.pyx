from .poly.polyvec cimport *
from .poly.polynomial cimport *
from .Kyberutils cimport *
import os
import hashlib

class Kyber:
    def __init__(self ,paramset):
        self.k = paramset.k
        self.eta_e = paramset.eta_e
        self.eta_s = paramset.eta_s
    def keygen(self , seed = None):
        if seed == None:
            seed = os.urandom(32)

        temp = hashlib.sha3_512(seed).digest()
        rho, sigma = temp[:32] , temp[32:]
        
        matA = gen_mat(rho , self.k)
        A = KyberMat(matA , self.k)
        self.A = KyberMat(A , self.k)

        slist = []
        for i in range(self.k):
            slist.append(CBD(sigma+bytes([i]) , self.k , self.eta_s))
        self.s = KyberVec(slist , self.k , 0)

        elist = []
        for i in range(self.k):
            elist.append(CBD(sigma+bytes([i+self.k]) , self.k , self.eta_e))
        e = KyberVec(elist , self.k , 0)

        self.s.to_ntt()
        e.to_ntt()
        self.t = KyberVec(None , self.k , 1)
        self.A.mul(self.t , self.s)
        self.t.add(self.t , e)
        

