from Crypto.Cipher import AES
from Kyber_Dilithium.Kyber import Kyber
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

print("start keygen")
print("--------------------------------------")
pk , sk = k.keygen()
print("complete, get")
print("--------------------------------------")
print("pk:({})\n".format(len(pk)) , pk)
print("--------------------------------------")
print("sk:({})\n".format(len(sk)) , sk)
print("--------------------------------------")

print("Alice start encrypt")
print("--------------------------------------")
Kmsg , c = Alice(pk)

print("Alice generate Kmsg:({})\n".format(len(Kmsg)), Kmsg)
print("--------------------------------------")
print("Alice generate c:({})\n".format(len(c)) , c)
print("--------------------------------------")
m = Bob(sk , Kmsg , c)
print("Bob start decrypt")
print("--------------------------------------")
print("Bob decrypt and get" , m)

print("--------------------------------------")
print("speed test")
import tqdm
for i in tqdm.tqdm(range(10000)):
    k.keygen()

for i in tqdm.tqdm(range(10000)):
    k.kemenc()

for i in tqdm.tqdm(range(10000)):
    k.kemdec(Kmsg)

'''
10000/10000 [00:33<00:00, 298.86it/s]
10000/10000 [00:15<00:00, 641.22it/s]
10000/10000 [00:21<00:00, 455.42it/s]
'''