from .decl cimport KyberPoly as KyberPoly_c
from .decl cimport DilithiumPoly as DilithiumPoly_c
from .decl cimport polyvec as polyvec_c
from .decl cimport polymat as polymat_c
cimport numpy as cnp
import numpy as np
from cpython.mem cimport PyMem_Malloc, PyMem_Free
cnp.import_array()

cdef Kybervecinit(polyvec_c[KyberPoly_c] **res ,int index, polylist , int k, int flag )
cdef class KyberVec:
    cdef polyvec_c[KyberPoly_c] *_core
    cdef int k

cdef class KyberMat:
    cdef polymat_c[KyberPoly_c] *_core
    cdef Matinit(self , list matlist , k)

