#include "polymat.h"
template <typename T, int k>
inline polymat<T, k>::polymat(polyvec<T,k> *veclist[]){
    for(int i = 0;i<k;i++){
        this->veclist[i] = veclist[i];
    }
}

template <typename T, int k>
inline void polymat<T, k>::right_mul(polyvec<T, k> *res, polyvec<T, k> *rvalue){
    for(int i = 0 ; i < k ;i++){
        this->veclist[i]->mul(res->datavec[i] , rvalue);
    }
}

template <typename T, int k>
inline void polymat<T, k>::trans(){
    T *temp;
    for(int i = 0; i < k-1;i++){
        for(int j = i+1; j < k ; j++){
            temp = this->veclist[i]->datavec[j];
            this->veclist[i]->datavec[j] = this->veclist[j]->datavec[i];
            this->veclist[j]->datavec[i] = temp;
        }
    }
}

template <typename T, int k>
inline polymat<T, k>::~polymat(){
    for(int i = 0;i<k;i++){
        delete veclist[i];
    }
}
