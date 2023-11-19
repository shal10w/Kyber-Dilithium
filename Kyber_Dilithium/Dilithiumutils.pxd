
from .Kyberutils cimport BitsToBytes , BytesToBits , Encode , Decode
from numpy cimport int32_t


cdef list rej_eta(int eta ,bytes seed ,int k)
cdef list ExpandA(bytes seed ,int k ,int l)
cdef list ExpandMask(bytes seed , int kapa , int l , int gamma)
cdef Decompose(list r ,int a)
cdef Power2Round(list r ,int d)
cdef HighBits(list r , int a)
cdef LowBits(list r , int a)
cdef bytes pack_vec(list vec , int k , int bit , int flag)
cdef list unpack_vec(bytes buf , int k , int bit , int flag)
cdef list SampleInBall(bytes seed ,int tau)
cdef int inf_norm(list vec)