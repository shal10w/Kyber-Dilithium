
from libcpp cimport bool
from libcpp.vector cimport vector
from numpy cimport int16_t

cdef vector[bool] BytesToBits(bytes B)

cdef list gen_vec(bytes seed)
cdef list gen_mat(bytes seed , int k)
cdef list CBD(bytes seed , int k)