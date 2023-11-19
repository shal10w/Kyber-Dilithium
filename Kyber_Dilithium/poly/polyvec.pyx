# distutils: language = c++

import numpy as np
cdef Kybervecinit(polyvec_c[KyberPoly_c] **res ,int index, polylist , int k, int flag ):
    cdef KyberPoly_c ** a
    cdef cnp.ndarray[cnp.int16_t] temp
    if polylist != None:
        a = <KyberPoly_c **>PyMem_Malloc(k*sizeof(KyberPoly_c**))
        for i in range(k):
            temp = np.array(polylist[i] , dtype=np.int16)
            a[i] = new KyberPoly_c(<cnp.int16_t*>temp.data, flag , flag)
        res[index] = new polyvec_c[KyberPoly_c](a , k)
        PyMem_Free(a)
    else:
        res[index] = new polyvec_c[KyberPoly_c](<KyberPoly_c**>0,k)
cdef class KyberVec:
    def __init__(self ,polylist ,int k , int flag):
        Kybervecinit(&self._core,0 , polylist , k , flag)
        self.k = k
    def add(self, KyberVec res ,KyberVec b):
        self._core.add(res._core , b._core)
    def to_ntt(self):
        self._core.to_ntt()
    def to_poly(self):
        self._core.to_poly()
    def mul(self , KyberPoly res , KyberVec b):
        self._core.mul(res._core , b._core)
    def getpoly(self , nttflag):
        res = []
        if nttflag == 0:
            for i in range(self.k):
                res.append(self._core.datavec[i].polyarray)
            return res
        else:
            for i in range(self.k):
                res.append(self._core.datavec[i].nttarray)
            return res
    
    def __dealloc__(self):
        del self._core
cdef class KyberMat:
    def __init__(self, matlist ,k):
        self.Matinit(matlist , k)
        self.k = k
    cdef Matinit(self , list matlist , k):
        cdef polyvec_c[KyberPoly_c] ** a
        a = <polyvec_c[KyberPoly_c] **>PyMem_Malloc(k*sizeof(KyberPoly_c**))
        for i in range(k):
            Kybervecinit(a,i , matlist[i] , k , 1)
        self._core = new polymat_c[KyberPoly_c](a , self.k)
        PyMem_Free(a)
    def mul(self , KyberVec res , KyberVec b):
        self._core.right_mul(res._core , b._core)
    def getpoly(self , nttflag):
        res = []
        if nttflag == 0:
            for i in range(self.k):
                res.append([self._core.veclist[i].datavec[j].polyarray for j in range(self.k)])
            return res
        else:
            for i in range(self.k):
                res.append([self._core.veclist[i].datavec[j].nttarray for j in range(self.k)])
            return res
    def trans(self):
        self._core.trans()
    def __dealloc__(self):
        del self._core


cdef Dilithiumvecinit(polyvec_c[DilithiumPoly_c] **res ,int index, polylist , int k, int flag ):
    cdef DilithiumPoly_c ** a
    cdef cnp.ndarray[cnp.int32_t] temp
    if polylist != None:
        a = <DilithiumPoly_c **>PyMem_Malloc(k*sizeof(DilithiumPoly_c**))
        for i in range(k):
            temp = np.array(polylist[i] , dtype=np.int32)
            a[i] = new DilithiumPoly_c(<cnp.int32_t*>temp.data, flag , flag)
        res[index] = new polyvec_c[DilithiumPoly_c](a , k)
        PyMem_Free(a)
    else:
        res[index] = new polyvec_c[DilithiumPoly_c](<DilithiumPoly_c**>0,k)
cdef class DilithiumVec:
    def __init__(self ,polylist ,int k , int flag):
        Dilithiumvecinit(&self._core,0 , polylist , k , flag)
        self.k = k
    def add(self, DilithiumVec res ,DilithiumVec b):
        self._core.add(res._core , b._core)
    def sub(self , DilithiumVec res , DilithiumVec b):
        self._core.sub(res._core , b._core)
    def to_ntt(self):
        self._core.to_ntt()
    def to_poly(self):
        self._core.to_poly()
    def mul(self , DilithiumPoly res , DilithiumVec b):
        self._core.mul(res._core , b._core)
    def polymul(self , DilithiumVec res , DilithiumPoly b):
        for i in range(self.k):
            self._core.datavec[i].mul(res._core.datavec[i] , b)
    def getpoly(self , nttflag):
        res = []
        if nttflag == 0:
            for i in range(self.k):
                res.append(self._core.datavec[i].polyarray)
            return res
        else:
            for i in range(self.k):
                res.append(self._core.datavec[i].nttarray)
            return res
    
    def __dealloc__(self):
        del self._core
cdef class DilithiumMat:
    def __init__(self, matlist ,k , l):
        self.Matinit(matlist , k , l)
        self.k = k
        self.l = l
    cdef Matinit(self , list matlist , k , l):
        cdef polyvec_c[DilithiumPoly_c] ** a
        a = <polyvec_c[DilithiumPoly_c] **>PyMem_Malloc(k*sizeof(DilithiumPoly_c**))
        for i in range(k):
            Dilithiumvecinit(a,i , matlist[i] , l , 1)
        self._core = new polymat_c[DilithiumPoly_c](a , k)
        PyMem_Free(a)
    def mul(self , DilithiumVec res , DilithiumVec b):
        self._core.right_mul(res._core , b._core)
    def getpoly(self , nttflag):
        res = []
        if nttflag == 0:
            for i in range(self.k):
                res.append([self._core.veclist[i].datavec[j].polyarray for j in range(self.l)])
            return res
        else:
            for i in range(self.k):
                res.append([self._core.veclist[i].datavec[j].nttarray for j in range(self.l)])
            return res
    def trans(self):
        self._core.trans()
    def __dealloc__(self):
        del self._core

