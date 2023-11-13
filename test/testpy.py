from Kyber_Dilithium import polynomial
import numpy

a = numpy.zeros((1,256) , dtype=numpy.int16)[0]
print(type(a))
a = polynomial.KyberPoly(a , 0 , 0)
print(a.polyarray)