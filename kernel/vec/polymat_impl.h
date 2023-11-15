#include <stdlib.h>
template <typename T>
inline polymat<T>::polymat(polyvec<T> *veclist[] , int k){
    this->veclist = (polyvec<T>**)malloc(k*sizeof(polyvec<T>**));
    for(int i = 0;i<k;i++){
        this->veclist[i] = veclist[i];
    }
    this->k = k;
}

template <typename T>
inline void polymat<T>::right_mul(polyvec<T> *res, polyvec<T> *rvalue){
    for(int i = 0 ; i < k ;i++){
        this->veclist[i]->mul(res->datavec[i] , rvalue);
    }
}

template <typename T>
inline void polymat<T>::trans(){
    T *temp;
    for(int i = 0; i < k-1;i++){
        for(int j = i+1; j < k ; j++){
            temp = this->veclist[i]->datavec[j];
            this->veclist[i]->datavec[j] = this->veclist[j]->datavec[i];
            this->veclist[j]->datavec[i] = temp;
        }
    }
}

template <typename T>
inline polymat<T>::~polymat(){
    for(int i = 0;i<k;i++){
        delete veclist[i];
    }
}
