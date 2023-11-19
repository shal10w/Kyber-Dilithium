#include <stdlib.h>
template <typename T>
inline polyvec<T>::polyvec(T *vec[] , int k){
    datavec = (T**)malloc(k*sizeof(T*));
    if(vec == NULL){
        for(int i = 0 ; i < k ;i++){
            datavec[i] = new T(0,1,1);
        }
    }
    else{
        for(int i = 0 ; i < k ;i++){
            datavec[i] = vec[i];
        }
    }
    this->k = k;
}

template <typename T>
inline void polyvec<T>::reset(int nttflag, int montflag){
    for(int i = 0 ; i < k ; i++){
        this->datavec[i]->reset(nttflag , montflag);
    }
}

template <typename T>
inline void polyvec<T>::mul(T *res, polyvec *rvalue){
    T *mid = new T(0 , 1, 1);
    for(int i = 0 ; i < k;i++){
        this->datavec[i]->mul(mid , rvalue->datavec[i]);
        res->poly_add(res , mid);
    }
    delete mid;
}
template <typename T>
inline void polyvec<T>::add(polyvec *res, polyvec *rvalue){
    for(int i = 0 ; i < k ; i++){
        this->datavec[i]->poly_add(res->datavec[i] , rvalue->datavec[i]);
    }
}
template <typename T>
inline void polyvec<T>::sub(polyvec *res, polyvec *rvalue){
    for(int i = 0 ; i < k ; i++){
        this->datavec[i]->poly_sub(res->datavec[i] , rvalue->datavec[i]);
    }
}
template <typename T>
inline void polyvec<T>::to_poly()
{
    for(int i = 0 ; i < k ; i++){
        this->datavec[i]->to_poly();
    }
}
template <typename T>
inline void polyvec<T>::to_ntt(){
    for(int i = 0 ; i < k ; i++){
        this->datavec[i]->to_ntt();
    }
}
template <typename T>
inline polyvec<T>::~polyvec()
{
    for(int i = 0;i<k;i++){
        delete datavec[i];
    }
    delete datavec;
}
