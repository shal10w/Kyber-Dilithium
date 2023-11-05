from Crypto.Util.number import *


def nttdata(q , R , r):
    reslist = [0]*256
    for i in range(256):
        pos = int(bin(i)[2:].rjust(8 , '0')[::-1] , 2)
        reslist[pos] = pow(r , i , q) * R % q
        if reslist[pos] > q/2:
            reslist[pos] -= q
    return reslist
def printformat(alist):
    output = '{\n\t'
    for i in range(len(alist)//8):
        for j in range(8):
            output += str(alist[i*8+j]).rjust(8 , ' ') + ','
        output += '\n\t'
    output += '};'
    print(output)
def nttdata_kyber(q , R , r):
    reslist = [0]*128
    for i in range(128):
        pos = int(bin(i)[2:].rjust(7 , '0')[::-1] , 2)
        reslist[pos] = pow(r , i , q) * R % q
        if reslist[pos] > q/2:
            reslist[pos] -= q
    return reslist
#printformat(nttdata(8380417 , 1<<32 , 1753))
printformat(nttdata_kyber(3329 , 1<<16 , 17))