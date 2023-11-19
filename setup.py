from setuptools import setup , Extension
from Cython.Build import cythonize
import numpy
kwds = {
    "language": "c++",
    "extra_link_args":["build/kernel/poly/libpoly.a"],
    "include_dirs":["numpy.get_include()"]
}
exts = [
    Extension("Kyber_Dilithium.poly.polynomial",["Kyber_Dilithium/poly/polynomial.pyx"] , **kwds),
    Extension("Kyber_Dilithium.poly.polyvec",["Kyber_Dilithium/poly/polyvec.pyx"] , **kwds),
    Extension("Kyber_Dilithium.Kyber" , ["Kyber_Dilithium/Kyber.pyx"] , **kwds),
    Extension("Kyber_Dilithium.Kyberutils" , ["Kyber_Dilithium/Kyberutils.pyx"] , **kwds),
    Extension("Kyber_Dilithium.Dilithium" , ["Kyber_Dilithium/Dilithium.pyx"] , **kwds),
    Extension("Kyber_Dilithium.Dilithiumutils" , ["Kyber_Dilithium/Dilithiumutils.pyx"] , **kwds)
]

setup(
    name = "Kyber_Dilithium",
    ext_modules=cythonize(exts , compiler_directives={'language_level' : "3"} , build_dir = "build"),
    packages=["Kyber_Dilithium"]
)