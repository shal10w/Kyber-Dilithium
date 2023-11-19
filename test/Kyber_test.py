from Crypto.Cipher import AES
from Kyber_Dilithium.Kyber import Kyber
import os
paramset = {
    "q":3329,
    "k":2,
    "eta1":2,
    "eta2":2,
    "du":10,
    "dv":4
}

def Alice(pk):
    secret = b"hello bob.-Alice"
    AliceKyber = Kyber(paramset)
    AliceKyber.load_pk(pk)
    Kmsg, K = AliceKyber.kemenc()
    print()
    aes = AES.new(key = K , mode = AES.MODE_ECB)
    c = aes.encrypt(secret)
    return Kmsg , c

def Bob(sk , Kmsg , c):
    BobKyber = Kyber(paramset)
    BobKyber.load_sk(sk)
    K = BobKyber.kemdec(Kmsg)
    aes = AES.new(key = K , mode = AES.MODE_ECB)
    m = aes.decrypt(c)
    return m
k = Kyber(paramset)

pk , sk = k.keygen()
#print("pk:({})".format(len(pk)) , pk)
#print("sk:({})".format(len(sk)) , sk)

Kmsg , c = Alice(pk)

print("Alice generate Kmsg", Kmsg)
#print("Alice generate c" , c)

m = Bob(sk , Kmsg , c)

print("Bob decrypt and get" , m)

# speed test
import tqdm
for i in tqdm.tqdm(range(10000)):
    k.keygen()

for i in tqdm.tqdm(range(10000)):
    k.kemenc()

for i in tqdm.tqdm(range(10000)):
    k.kemdec(c)