from Kyber_Dilithium.Dilithium import *

paramset = {
    "q":8380417,
    "k":4,
    "l":4,
    "eta":2,
    "d":13,
    "loggamma1":17,
    "gamma2":(8380417-1)//88,
    "tau":39,
    "omega":80
}

def Alice(m , sk):
    dAlice = Dilithium(paramset)
    dAlice.load_sk(sk)
    s = dAlice.sign(m)
    return s

def Bob(m , s , pk):
    dBob = Dilithium(paramset)
    dBob.load_pk(pk)
    return dBob.verify(m , s)


d = Dilithium(paramset)
print("start keygen")
print("--------------------------------------")
pk , sk = d.keygen()
print("complete, get")
print("--------------------------------------")
print("pk:({})\n".format(len(pk)) , pk)
print("--------------------------------------")
print("sk:({})\n".format(len(sk)) , sk)
print("--------------------------------------")

print("Alice start sign")
print("--------------------------------------")
s = Alice(b"sign message" , sk)
print("Alice generate signature for message b'sign message':({})\n".format(len(s)) , s)
print("--------------------------------------")
print("Bob start verify")
print("--------------------------------------")
v = Bob(b"sign message" , s , pk)
print("Bob verify true message with true signature")
print(v)
print("--------------------------------------")
print("Bob verify wrong message with true signature")
v = Bob(b"wrong message" , s , pk)
print(v)
_s = b'\x00' + s[1:]
v = Bob(b"sign message" , _s , pk)
print("--------------------------------------")
print("Bob verify true message with wrong signature")
print(v)

print("--------------------------------------")
print("speed test")
import tqdm
for i in tqdm.tqdm(range(10000)):
    d.keygen()

clist = []
for i in tqdm.tqdm(range(10000)):
    clist.append(d.sign(str(i).encode()))

for i in tqdm.tqdm(range(10000)):
    d.verify(str(i).encode() , clist[i])

'''
10000/10000 [00:42<00:00, 233.14it/s]
10000/10000 [01:47<00:00, 92.66it/s]
10000/10000 [00:27<00:00, 357.50it/s]
'''