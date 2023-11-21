

bdmk(){
    mkdir build
    cd build
    cmake .. && make
    cd ..
    cp -r ./kernel/vec ./build/kernel/vec
}
bdcy(){
    python ./setup.py build_ext
}
bdclean(){
    cd build
    make clean
    rm -r temp.linux-x86_64-3.9 Kyber_Dilithium kernel test CMakeFiles
    rm cmake_install.cmake CMakeCache.txt Makefile
    mv lib.linux-x86_64-3.9/Kyber_Dilithium ./Kyber_Dilithium
    rm -r lib.linux-x86_64-3.9
    cd ..
}
build(){
    bdmk
    bdcy
    bdclean
    cp ./test/Kyber_test.py ./build/Kyber_test.py
    cp ./test/Dilithium_test.py ./build/Dilithium_test.py
}
clean(){
    rm -r build
}

$1