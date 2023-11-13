from setuptools import setup , Extension
from Cython.Build import cythonize


exts = [
    Extension("Kyber_Dilithium.polynomial",["Kyber_Dilithium/polynomial.pyx"] , extra_link_args = ["build/poly/libpoly.a"]),
]

setup(
    name = "Kyber_Dilithium",
    ext_modules=cythonize(exts , compiler_directives={'language_level' : "3"} , build_dir = "build"),
    packages=["Kyber_Dilithium"]
)