
build(){
    mkdir build
    cd build
    cmake .. && make
    cd .. && python ./setup.py build_ext
}

clean(){
    rm -r build
}

$1