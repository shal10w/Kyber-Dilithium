
import hashlib
from Crypto.Hash import SHAKE256


cdef list rej_eta(int eta ,bytes seed ,int k):
    cdef list res , bitlist , templist
    cdef bytes buf
    cdef int nbit , blocknum , pos , temp
    res = []
    pos = 0
    nbit = len(bin(2*eta+1))-2
    blocknum = int(nbit * 32 * k * (2**nbit) / (2*eta+1) / 136)+2
    buf = hashlib.shake_256(seed).digest(blocknum * 136)
    bitlist = BytesToBits(buf)
    for i in range(k):
        templist = []
        while len(templist) < 256:
            temp = 0
            for x in range(nbit):
                temp <<=1
                temp += bitlist[pos]
                pos += 1
            if temp < (2*eta+1):
                templist.append(eta - temp)
        res.append(templist)
    return res

cdef list ExpandA(bytes seed ,int k ,int l):
    cdef int pos , magic_num
    cdef int32_t temp1
    cdef list res , line , polyarray
    shake = hashlib.shake_256(seed)
    res = []
    pos = 0
    magic_num = 6*k*l # num(dilithium_n * 3) * error_rate(1<<23 / 8380417) * block_size(136) + 1
    buf = shake.digest(magic_num * 136) 
    for i in range(k):
        line = []
        for j in range(l):
            polyarray = []
            while len(polyarray) < 256:
                temp1 = buf[pos] + (buf[pos+1] << 8) + ((buf[pos+2]&0x7f)<<16)
                if temp1 < 8380417:
                    polyarray.append(temp1)
                pos += 3
            line.append(polyarray)
        res.append(line)
    return res

cdef list ExpandMask(bytes seed , int kapa , int l , int loggamma):
    cdef int pos
    cdef int32_t temp
    cdef list res , line , bitlist
    cdef bytes buf
    res = []
    
    for i in range(l):
        shake = hashlib.shake_256(seed+bytes([(kapa+i)&0xff , (kapa+i)>>256]))
        buf = shake.digest((loggamma+1)*32)
        bitlist = BytesToBits(buf)
        line = []
        pos = 0
        for j in range(256):
            temp = 0
            for k in range(loggamma):
                temp <<= 1
                temp += bitlist[pos]
                pos += 1
            line.append(temp)
        res.append(line)
    return res

cdef Decompose(list r ,int a):
    cdef list r1 , r0
    cdef int a_2
    cdef int q , r0int , r1int
    q = 8380417
    r1 = []
    r0 = []
    a_2 = a//2
    for i in r:
        if i < 0:
            r1int = i + q
        else:
            r1int = i
        r0int = (r1int % a)
        if r0int > a_2:
            r0int -= a
        if r1int - r0int == q-1:
            r1.append(0)
            r0.append(r0int-1)
        else:
            r1.append((r1int-r0int)//a)
            r0.append(r0int)
    return r1 , r0
cdef Power2Round(list r ,int d):
    return Decompose(r , 1<<d)

cdef HighBits(list r , int a):
    return Decompose(r ,a)[0]
cdef LowBits(list r , int a):
    return Decompose(r , a)[1]
cdef bytes pack_vec(list vec , int k , int bit , int flag):
    cdef bytes res
    res = b''
    for i in range(k):
        if flag == 1:
            res += Encode([(1<<bit)-1-j for j in vec[i]] , bit+1)
        else:
            res += Encode(vec[i] , bit)
    return res

cdef list unpack_vec(bytes buf , int k , int bit , int flag):
    cdef list res , temp
    res = []
    for i in range(k):
        if flag == 1:
            temp = Decode(buf[i*32*(bit+1):i*32*(bit+1)+32*(bit+1)] ,bit+1)
            res.append([(1<<bit)-1-j for j in temp])
        else:
            res.append(Decode(buf[i*32*bit:i*32*bit+32*bit] , bit))
    return res

cdef list SampleInBall(bytes seed ,int tau):
    cdef list res,signlist
    cdef int pos , b , signpos
    cdef bytes buf
    res = [0]*256
    signpos,pos = 0,0
    shake = SHAKE256.new()
    shake.update(seed)
    signlist = BytesToBits(shake.read(8))
    buf = shake.read(136)
    for i in range(256-tau , 256):
        if pos == 136:
            buf = shake.read(136)
            pos = 0
        b = buf[pos]
        pos += 1
        while b > i:
            b = buf[pos]
            pos += 1
        res[i] = res[b]
        res[b] = 1 - 2*signlist[signpos]
        signpos += 1
    return res

cdef int inf_norm(list vec):
    cdef int res
    res = abs(vec[0][0])
    for i in vec:
        for j in range(256):
            if i[j]>res:
                res = i[j]
            elif -i[j] > res:
                res = -i[j]
    return res

cdef tuple MakeHint(list z , list r , int a):
    cdef list r1 , v1 , res , line
    cdef int cnt 
    res = []
    cnt = 0
    for i in range(len(z)):
        r1 = HighBits(r[i] , a)
        v1 = HighBits(z[i] , a)
        line = []
        for j in range(256):
            if r1[j] == v1[j]:
                line.append(0)
            else:
                line.append(1)
                cnt += 1
        res.append(line)
    return res , cnt

cdef list UseHint(list h , list r , int a):
    cdef int m 
    cdef list res , r0 , r1
    m = 8380416//a
    res = []
    for i in range(len(r)):
        r1 , r0 = Decompose(r[i] , a)
        for j in range(256):
            if h[i][j] == 1:
                if r0[j] > 0:
                    r1[j] = (r1[j] + 1) % m
                else:
                    r1[j] = (r1[j] - 1) % m
        res.append(r1)
    return res

cdef int cnt_one(list h):
    cdef cnt , hlen
    hlen = len(h)
    cnt = 0
    for i in range(hlen):
        for j in range(256):
            if h[i][j] == 1:
                cnt += 1
    return cnt