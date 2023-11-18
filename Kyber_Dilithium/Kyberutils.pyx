from hashlib import *

cdef bytes BitsToBytes(list b):
    cdef list res
    cdef int temp
    res = []
    for i in range(len(b)//8):
        temp = 0
        for j in range(8):
            temp += b[(i<<3)+j] << j
        res.append(temp)
    return bytes(res)
cdef list BytesToBits(bytes B):
    cdef list res
    cdef int a
    a = len(B)
    res = []
    for i in range(a):
        for j in range(8):
            res.append((B[i] >> j) & 1)
    return res

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
        if temp2 < 3329 and reslen < 256:
            res.append(temp2)
            reslen += 1
    return res

cdef list gen_mat(bytes seed ,int k):
    cdef list A
    cdef list temp
    A = []
    for i in range(k):
        temp = []
        for j in range(k):
            temp.append(gen_vec(seed+bytes([j,i])))
        A.append(temp)
    return A


cdef list CBD(bytes seed , int eta):
    cdef list res, bufbits
    cdef int pos , a,b , bufnum
    res = []
    buf = shake_256(seed).digest(eta*64)
    bufbits = BytesToBits(buf)
    for i in range(256):
        a = 0
        b = 0
        for j in range(eta):
            a += bufbits[2*eta*i+j]
            b += bufbits[2*eta*i+eta+j]
        res.append(a - b)
    return res

cdef list Decode(bytes buf ,int bitlen):
    cdef list res , bufbit
    cdef int temp
    res = []
    bufbit = BytesToBits(buf)
    for i in range(256):
        temp = 0
        for j in range(bitlen):
            temp += bufbit[i*bitlen+j] << j
        res.append(temp)
    return res

cdef bytes Encode(list polyarray , int bitlen):
    cdef list midres
    midres = []
    for i in range(len(polyarray)):
        for j in range(bitlen):
            midres.append((polyarray[i] >> j)&1)
    return BitsToBytes(midres)

cdef list plus_mod(list array , int q):
    cdef list res
    res = []
    for i in array:
        if i > 0:
            res.append(i)
        else:
            res.append(i+q)
    return res

cdef list Compress(int q , list vec ,int d):
    cdef list res
    cdef int module
    module = 1<<d
    res = []
    for i in vec:
        res.append(round(i*module / q) % module)
    return res

cdef list Decompress(int q , list vec ,int d):
    cdef list res
    cdef int module
    module = 1<<d
    res = []
    for i in vec:
        res.append(round(i*q/module))
    return res

