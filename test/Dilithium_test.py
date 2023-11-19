from Kyber_Dilithium.Dilithium import *
from Kyber_Dilithium.poly.polynomial import *
from Kyber_Dilithium.poly.polyvec import *
from Kyber_Dilithium.Dilithiumutils import *

paramset = {
    "q":8380417,
    "k":4,
    "l":4,
    "eta":2,
    "d":13,
    "loggamma1":17,
    "gamma2":(8380417-1)//88,
    "tau":39
}

d = Dilithium(paramset)

pk , sk = d.keygen()

s1list = d.t0.getpoly(0)
print(s1list)

d.load_sk(sk)

_s1 = d.t0.getpoly(0)
print(_s1)
print(_s1 == s1list)