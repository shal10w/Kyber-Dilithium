#include <thread>

template <typename T, int k>
inline polyvec<T, k>::polyvec(T *vec[]){
    for(int i = 0 ; i < k ;i++){
        datavec[i] = vec[i];
    }
}

template <typename T, int k>
void polyvec<T, k>::mul(T *res, polyvec *rvalue){

}
