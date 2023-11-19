

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
build(){
    bdmk
    bdcy
    cp ./test/Kyber_test.py ./build/lib.linux-x86_64-3.9/Kyber_test.py
    cp ./test/Dilithium_test.py ./build/lib.linux-x86_64-3.9/Dilithium_test.py
}
clean(){
    rm -r build
}

$1