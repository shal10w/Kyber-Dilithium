# distutils: language = c++
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
    cdef Matinit(self , list matlist , k):
        cdef polyvec_c[KyberPoly_c] ** a
        a = <polyvec_c[KyberPoly_c] **>PyMem_Malloc(k*sizeof(KyberPoly_c**))
        for i in range(k):
            Kybervecinit(a,i , matlist[i] , k , 1)
        self._core = new polymat_c[KyberPoly_c](a , 2)
        PyMem_Free(a)
    def mul(self , KyberVec res , KyberVec b):
        self._core.right_mul(res._core , b._core)
    
    def trans(self):
        self._core.trans()
    def __dealloc__(self):
        del self._core

