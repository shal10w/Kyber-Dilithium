# distutils: language = c++
import numpy as np


cdef class KyberPoly:
    def __init__(self , numlist,int nttflag , int montflag):
        cdef cnp.ndarray[cnp.int16_t] temp
        if numlist == None:
            self._core = new KyberPoly_c(<cnp.int16_t *>0 , nttflag , montflag)
        else:
            temp = np.array(numlist , dtype = np.int16)
            self._core = new KyberPoly_c(<cnp.int16_t *>temp.data , nttflag , montflag)
    def add(self , KyberPoly res , KyberPoly rvalue):
        self._core.poly_add(res._core , rvalue._core)
    def sub(self , KyberPoly res , KyberPoly rvalue):
        self._core.poly_sub(res._core , rvalue._core)
    def mul(self , KyberPoly res , KyberPoly rvalue):
        self._core.mul(res._core , rvalue._core)
    def to_poly(self):
        self._core.to_poly()
    def to_ntt(self):
        self._core.to_ntt()
    @property
    def nttarray(self):
        return self._core.nttarray
    @property
    def polyarray(self):
        return self._core.polyarray
    def __dealloc__(self):
        del self._core
    
cdef class DilithiumPoly:
    def __init__(self , numlist,int nttflag , int montflag):
        cdef cnp.ndarray[cnp.int32_t] temp
        if numlist == None:
            self._core = new DilithiumPoly_c(<cnp.int32_t *>0 , nttflag , montflag)
        else:
            temp = np.array(numlist , dtype = np.int32)
            self._core = new DilithiumPoly_c(<cnp.int32_t *>temp.data , nttflag , montflag)
    def add(self , DilithiumPoly res , DilithiumPoly rvalue):
        self._core.poly_add(res._core , rvalue._core)
    def sub(self , DilithiumPoly res , DilithiumPoly rvalue):
        self._core.poly_sub(res._core , rvalue._core)
    def mul(self , DilithiumPoly res , DilithiumPoly rvalue):
        self._core.mul(res._core , rvalue._core)
    def to_poly(self):
        self._core.to_poly()
    def to_ntt(self):
        self._core.to_ntt()
    @property
    def nttarray(self):
        return self._core.nttarray
    @property
    def polyarray(self):
        return self._core.polyarray
    def __dealloc__(self):
        del self._core