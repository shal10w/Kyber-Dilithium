# distutils: language = c++



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
    def __dealloc__(self):
        del self._core
    