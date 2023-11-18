#ifndef DEBUG_H
#define DEBUG_H
#include <iostream>

template <typename T>
void output(T *a , const char *b){
    std::cout << b << " ";
    for(int i = 0 ; i < 10;i++){
        std::cout << a[i] << " ";
    }
    std::cout << std::endl;
}
#endif