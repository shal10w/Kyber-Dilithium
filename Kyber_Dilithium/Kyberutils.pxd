
from numpy cimport int16_t

cdef bytes BitsToBytes(list b)
cdef list BytesToBits(bytes B)
cdef list gen_vec(bytes seed)
cdef list gen_mat(bytes seed , int k)
cdef list CBD(bytes seed , int eta)
cdef list Decode(bytes buf , int bitlen)
cdef bytes Encode(list polyarray , int bitlen)
cdef list plus_mod(list array , int q)
cdef list Compress(int q , list vec ,int d)
cdef list Decompress(int q , list vec ,int d)
cdef bytes pack_vec(list vec , int k , int d , int q)
cdef list unpack_vec(bytes buf , int k , int d)