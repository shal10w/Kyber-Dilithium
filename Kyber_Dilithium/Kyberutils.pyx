from hashlib import *

cdef vector[bool] BytesToBits(bytes B):
    cdef vector[int] res
    cdef int a
    a = len(B)
    for i in range(a):
        pass

cdef list gen_vec(bytes seed):
    cdef int pos , reslen, magic_num
    cdef int16_t temp1 , temp2
    cdef list res
    shake = shake_128(seed)
    res = []
    reslen = 0
    pos = 0
    magic_num = 504 # num(kyber_n * 3 / 2) * error_rate(1<<12 / 3329) * block_size(168)
    buf = shake.digest(504) 
    while reslen < 256:
        if pos == magic_num:
            buf = shake.digest(504+168)
        temp1 = ((buf[pos+0] >> 0) | (buf[pos+1] << 8)) & 0xFFF
        temp2 = ((buf[pos+1] >> 4) | (buf[pos+2] << 4)) & 0xFFF
        pos += 3
        if temp1 < 3329:
            res.append(temp1)
            reslen+=1
        if temp2 < 3329:
            res.append(temp2)
            reslen += 1
    print(pos)
    return res

cdef list gen_mat(bytes seed ,int k):
    cdef list A
    A = []
    for i in range(k):
        for j in range(k):
            A.append(gen_vec(seed+bytes([j,i])))
    return A


cdef list CBD(bytes seed ,int k, int eta):
    cdef list res, and_list
    cdef int pos , temp1,temp2 , bufnum
    res = []
    buf = shake_256(seed).digest(((eta*256)//(8*136)+1)*136)
    pos = 0
    and_list = [0xc0 ,0x30 , 0xc , 0x3]
    for i in range(256):
        temp1 = 0
        temp2 = 0
        for j in range(eta):
            bufnum = (buf[pos>>2] & (and_list[pos&3]))>>((pos&3)<<1)
            temp1 += bufnum>>1
            temp2 += bufnum & 1
        res.append(temp1 - temp2)
    return res



