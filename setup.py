from setuptools import setup , Extension
from Cython.Build import cythonize
import numpy

exts = [
    Extension("Kyber_Dilithium.polynomial",["Kyber_Dilithium/polynomial.pyx"] , extra_link_args = ["build/kernel/poly/libpoly.a"],include_dirs=[numpy.get_include()]),
    Extension("Kyber_Dilithium.polyvec",["Kyber_Dilithium/polyvec.pyx"] , extra_link_args = ["build/kernel/poly/libpoly.a"],include_dirs=[numpy.get_include()])
]

setup(
    name = "Kyber_Dilithium",
    ext_modules=cythonize(exts , compiler_directives={'language_level' : "3"} , build_dir = "build"),
    packages=["Kyber_Dilithium"]
)