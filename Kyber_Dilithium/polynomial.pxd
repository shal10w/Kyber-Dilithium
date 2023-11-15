from decl cimport KyberPoly as KyberPoly_c
from decl cimport DilithiumPoly as DilithiumPoly_c




cdef class KyberPoly(object):
    cdef KyberPoly_c *_core

cdef class DilithiumPoly(object):
    cdef DilithiumPoly_c *_core