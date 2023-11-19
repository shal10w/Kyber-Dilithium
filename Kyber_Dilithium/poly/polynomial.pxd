from .decl cimport KyberPoly as KyberPoly_c
from .decl cimport DilithiumPoly as DilithiumPoly_c
cimport numpy as cnp

cnp.import_array()

cdef class KyberPoly:
    cdef KyberPoly_c *_core
    

cdef class DilithiumPoly:
    cdef DilithiumPoly_c *_core