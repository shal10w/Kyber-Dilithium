# distutils: language = c++



cdef class KyberPoly:
    def __init__(self , numlist,int nttflag , int montflag):
        cdef cnp.ndarray[cnp.int16_t] temp
        if numlist == None:
            self._core = new KyberPoly_c(<cnp.int16_t *>0 , nttflag , montflag)
        else:
            temp = np.array(numlist , dtype = np.int16)
            self._core = new KyberPoly_c(<cnp.int16_t *>temp.data , nttflag , montflag)
    @property
    def polyarray(self):
        return self._core.polyarray
    @property
    def nttarray(self):
        return self._core.nttarray
    def __dealloc__(self):
        del self._core
    