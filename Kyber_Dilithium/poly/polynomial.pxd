from .decl cimport KyberPoly as KyberPoly_c
cimport numpy as cnp

cnp.import_array()

cdef class KyberPoly:
    cdef KyberPoly_c *_core
    