# distutils: language = c++

from decl cimport KyberPoly as KyberPoly_c
from decl cimport DilithiumPoly as DilithiumPoly_c
from decl cimport polyvec as polyvec_c
from decl cimport polymat as polymat_c
cimport numpy as cnp
from cpython.mem cimport PyMem_Malloc, PyMem_Free
cnp.import_array()


cdef class Kyberpolyvec:
    cdef polyvec_c[KyberPoly_c] *_core
    def __init__(self ,cnp.ndarray[cnp.int16_t] polylist ,int k , int flag):
        self.Kyberinit(polylist , k , flag)
    cdef Kyberinit(self , cnp.ndarray[cnp.int16_t] polylist,int k , int flag):
        cdef KyberPoly_c ** a 
        if polylist != None:
            a = <KyberPoly_c **>PyMem_Malloc(k*sizeof(KyberPoly_c*))
            for i in range(k):
                a[i] = new KyberPoly_c(<cnp.int16_t*>polylist.data[i] , flag , flag)
            self._core = new polyvec_c[KyberPoly_c](a , k)
            PyMem_Free(a)
        else:
            self._core = new polyvec_c[KyberPoly_c](<KyberPoly_c**>0,k)
        
    cdef add(self, Kyberpolyvec res ,Kyberpolyvec b):
        self._core.add(res._core , b._core)

