

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
}
clean(){
    rm -r build
}

$1