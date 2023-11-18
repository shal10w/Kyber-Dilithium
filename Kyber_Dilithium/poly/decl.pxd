

from libc.stdint cimport int16_t , int32_t
cdef extern from "../../kernel/poly/poly.h":
    pass
cdef extern from "../../kernel/poly/Kyberpoly.h":
    cdef cppclass KyberPoly:
        int16_t[256] polyarray
        int16_t[256] nttarray
        KyberPoly(int16_t *array , int nttflag , int montflag)
        void reset(int nttflag , int montflag)
        void mul(KyberPoly *a , KyberPoly *b)
        void poly_add(KyberPoly *a , KyberPoly *b)
        void poly_sub(KyberPoly *a , KyberPoly *b)
        void to_poly()
        void to_ntt()
        void getpoly(int16_t *reslist)

cdef extern from "../../kernel/poly/Dilithiumpoly.h":
    cdef cppclass DilithiumPoly:
        int32_t[256] polyarray
        int32_t[256] nttarray
        DilithiumPoly(int32_t *array , int nttflag , int montflag)
        void reset(int nttflag , int montflag)
        void mul(DilithiumPoly *a , DilithiumPoly *b)
        void poly_add(KyberPoly *a , KyberPoly *b)
        void poly_sub(KyberPoly *a , KyberPoly *b)
        void to_poly()
        void to_ntt()
        void getpoly(int16_t *reslist)

cdef extern from "../../kernel/vec/polyvec.h":
    cdef cppclass polyvec[T]:
        T** datavec
        polyvec(T * vec[] , int k)
        void reset(int nttflag , int montflag)
        void mul(T*res , polyvec* rvalue)
        void add(polyvec *res , polyvec *rvalue)
        void to_poly()
        void to_ntt()

cdef extern from "../../kernel/vec/polymat.h":
    cdef cppclass polymat[T]:
        polyvec[T] **veclist
        polymat(polyvec[T] *veclist[] , int k)
        void right_mul(polyvec[T]*res , polyvec[T] *rvalue)
        void trans()


