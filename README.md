# Kyber-Dilithium

my homework of Modern Cryptography.

implementation of Kyber and Dilithium.

## build

### require

+ `cmake`
+ python packages `cython`, `pycryptodome`, `numpy`, install with `pip install cython pycryptodome numpy`

### compile and test

compile
```sh
./setup.sh build
```
test
```sh
python ./build/Kyber_test.py
python ./build/Dilithium_test.py
```