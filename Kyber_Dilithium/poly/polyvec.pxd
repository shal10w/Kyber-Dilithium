from .decl cimport KyberPoly as KyberPoly_c
from .decl cimport DilithiumPoly as DilithiumPoly_c
from .decl cimport polyvec as polyvec_c
from .decl cimport polymat as polymat_c
from .polynomial cimport KyberPoly , DilithiumPoly
cimport numpy as cnp

from cpython.mem cimport PyMem_Malloc, PyMem_Free
cnp.import_array()

cdef Kybervecinit(polyvec_c[KyberPoly_c] **res ,int index, polylist , int k, int flag )
cdef class KyberVec:
    cdef polyvec_c[KyberPoly_c] *_core
    cdef int k

cdef class KyberMat:
    cdef polymat_c[KyberPoly_c] *_core
    cdef int k
    cdef Matinit(self , list matlist , k)

cdef class DilithiumVec:
    cdef polyvec_c[DilithiumPoly_c] *_core
    cdef int k

cdef class DilithiumMat:
    cdef polymat_c[DilithiumPoly_c] *_core
    cdef int k
    cdef int l
    cdef Matinit(self , list matlist , k , l)