from hashlib import *
from libcpp cimport bool
from libcpp.vector cimport vector
def Parse(seedbytes):
    pass


cdef vector[bool] BytesToBits(bytes B):
    cdef vector[int] res
    int a
    a = len(B)
    for i in range(a):
        pass

cdef 