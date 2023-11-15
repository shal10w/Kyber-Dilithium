#include "polyvec.h"
template <typename T, int k>
inline polyvec<T, k>::polyvec(T *vec[]){
    if(vec == NULL){
        for(int i = 0 ; i < k ;i++){
            datavec[i] = new T(0,1,1);
        }
    }
    else{
        for(int i = 0 ; i < k ;i++){
            datavec[i] = vec[i];
            if(vec[i]->nttflag != 1){
                vec[i]->to_ntt();
            }
        }
    }
}

template <typename T, int k>
inline void polyvec<T, k>::reset(int nttflag, int montflag){
    for(int i = 0 ; i < k ; i++){
        this->datavec[i]->reset(nttflag , montflag);
    }
}

template <typename T, int k>
inline void polyvec<T, k>::mul(T *res, polyvec *rvalue){
    T *mid = new T(0 , 1, 1);
    for(int i = 0 ; i < k;i++){
        mid->mul(this->datavec[i] , rvalue->datavec[i]);
        res->poly_add(res , mid);
    }
    delete mid;
}
template <typename T, int k>
inline void polyvec<T, k>::add(polyvec *res, polyvec *rvalue){
    for(int i = 0 ; i < k ; i++){
        this->datavec[i]->poly_add(res->datavec[i] , rvalue->datavec[i]);
    }
}
template <typename T, int k>
inline void polyvec<T, k>::to_poly()
{
    for(int i = 0 ; i < k ; i++){
        this->datavec[i]->to_poly();
    }
}
template <typename T, int k>
inline void polyvec<T, k>::to_ntt(){
    for(int i = 0 ; i < k ; i++){
        this->datavec[i]->to_ntt();
    }
}
template <typename T, int k>
inline polyvec<T, k>::~polyvec()
{
    for(int i = 0;i<k;i++){
        delete datavec[i];
    }
}
