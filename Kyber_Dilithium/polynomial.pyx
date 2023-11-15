# distutils: language = c++
#from decl cimport KyberPoly as KyberPoly_c
cimport numpy as cnp
cnp.import_array()
cdef class KyberPoly:
    def __init__(self , 
    cnp.ndarray[cnp.int16_t] numlist,
    int nttflag , int montflag):
        self._core = new KyberPoly_c(<cnp.int16_t *>numlist.data , nttflag , montflag)
#    def __init__(self , int nttflag , int montflag):
#        self._core = new KyberPoly_c(<cnp.int16_t *>0 , nttflag , montflag)
    @property
    def polyarray(self):
        return self._core.polyarray
    @property
    def nttarray(self):
        return self._core.nttarray
    def __dealloc__(self):
        del self._core
    