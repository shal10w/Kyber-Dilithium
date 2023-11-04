#include "poly.h"
#include "reduce.h"

template <typename T, typename DT>
Polynomial<T , DT>::Polynomial(T *array, int nttflag):nttflag(nttflag){
    if(nttflag == 0){
        if(array){
            std::memcpy(this->polyarray , array , 256*sizeof(T));
        }
        else{
            std::memset(this->polyarray , 0 , 256*sizeof(T));
        }
    }
    else{
        if(array){
            std::memcpy(this->nttarray , array , 256*sizeof(T));
        }
        else{
            std::memset(this->nttarray , 0 , 256*sizeof(T));
        }
    }
}
template <typename T, typename DT>
void Polynomial<T,DT>::add(Polynomial *res , Polynomial *b){
    if(this->nttflag){
        for(int i = 0; i < 256 ; i++){
            res->nttarray[i] = mod_plus(this->nttarray[i] , b->nttarray[i] , this->q);
        }
    }
    else{
        for(int i = 0 ; i < 256 ; i++){
            res->polyarray[i] = mod_plus(this->polyarray[i] , b->polyarray[i] , this->q);
        }
    }
}
template <typename T, typename DT>
void Polynomial<T,DT>::sub(Polynomial *res , Polynomial *b){
    if(this->nttflag){
        for(int i = 0; i < 256 ; i++){
            res->nttarray[i] = mod_sub<T>(this->nttarray[i] , b->nttarray[i] , this->q);
        }
    }
    else{
        for(int i = 0 ; i < 256 ; i++){
            res->polyarray[i] = mod_sub<T>(this->polyarray[i] , b->polyarray[i] , this->q);
        }
    }
}
template <typename T, typename DT>
void Polynomial<T,DT>::to_mont(){
    for(int i = 0;i < 256;i++){
        this->nttarray[i] = this->mod_mul(this->nttarray[i] , this->R2modq);
    }
}
template <typename T, typename DT>
void Polynomial<T,DT>::rev_mont(){
    for(int i = 0;i < 256;i++){
        this->nttarray[i] = this->mod_mul(this->nttarray[i] , 1);
    }
}
template <typename T, typename DT>
void Polynomial<T,DT>::getpoly(T *reslist){
    if(this->nttflag){
        std::memcpy(reslist , this->nttarray , 256*sizeof(T));
    }
    else{
        std::memcpy(reslist , this->polyarray , 256*sizeof(T));
    }
}
template <typename T, typename DT>
T Polynomial<T,DT>::mod_mul(T a , T b){
    return montgomery_reduce<T , DT>((DT)a * b , this->qinv , this->q , this->qbit);
}

template <typename T, typename DT>
T Polynomial<T, DT>::mod(T a){
    
    return T();
}

/*
void Polynomial::mul(Polynomial *c){
    if(this->nttflag == 0){
        printf("Multiply forbidden");
        return ;
    }
    for(int i = 0; i < 512 ; i++){
        this->nttarray[i] *= c->nttarray[i];
        this->nttarray[i] %= this->q;
    }
}
*/

template class Polynomial<int16_t , int32_t>;
template class Polynomial<int32_t , int64_t>;