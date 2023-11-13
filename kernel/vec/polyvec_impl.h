#include <thread>

template <typename T, int k>
inline polyvec<T, k>::polyvec(T *vec[]){
    for(int i = 0 ; i < k ;i++){
        datavec[i] = vec[i];
        if(vec[i]->nttflag != 1){
            vec[i]->to_ntt();
        }
    }
}
template <typename T>
inline void multhread(T* res , T*a , T*b){
    res->mul(a , b);
}


template <typename T, int k>
inline void polyvec<T, k>::mul(T *res, polyvec *rvalue){
    std::thread *pool[k];
    T *mid[k];
    for(int i = 0;i < k ;i++){
        mid[i] = new T(NULL , 1, 1);
        pool[i] = new std::thread(multhread , mid[i] , this->datavec[i] , rvalue->datavec[i]);
    }
    for(int i = 0;i < k;i++){
        pool[i]->join();
        delete pool[i];
    }
    for(int i = 0;i<k;i++){
        res->add(res , mid[i]);
        delete mid[i];
    }
}
template <typename T, int k>
inline polyvec<T, k>::~polyvec(){
    for(int i = 0;i<k;i++){
        delete datavec[i];
    }
}
