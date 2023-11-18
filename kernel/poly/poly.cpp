#include "poly.h"
#include "reduce.h"

template <typename T, typename DT>
Polynomial<T , DT>::Polynomial(T *array, int nttflag , int montflag):nttflag(nttflag),montflag(montflag){
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
void Polynomial<T, DT>::reset(int nttflag, int montflag){
    std::memset(this->polyarray , 0 , 256*sizeof(T));
    std::memset(this->nttarray , 0 , 256*sizeof(T));
    this->nttflag = nttflag;
    this->montflag = montflag;
}
template <typename T, typename DT>
void Polynomial<T, DT>::poly_add(Polynomial *res, Polynomial *b)
{
    if(this->nttflag){
        for(int i = 0; i < 256 ; i++){
            res->nttarray[i] = mod(this->nttarray[i] + b->nttarray[i]);
        }
    }
    else{
        for(int i = 0 ; i < 256 ; i++){
            res->polyarray[i] = mod(this->polyarray[i] + b->polyarray[i]);
        }
    }
}
template <typename T, typename DT>
void Polynomial<T,DT>::poly_sub(Polynomial *res , Polynomial *b){
    if(this->nttflag){
        for(int i = 0; i < 256 ; i++){
            res->nttarray[i] = mod(this->nttarray[i] - b->nttarray[i]);
        }
    }
    else{
        for(int i = 0 ; i < 256 ; i++){
            res->polyarray[i] = mod(this->polyarray[i] - b->polyarray[i]);
        }
    }
}
template <typename T, typename DT>
void Polynomial<T,DT>::to_mont(){
    if(montflag == 1){
        return ;
    }
    montflag = 1;
    if(nttflag==0){
        for(int i = 0;i < 256;i++){
            this->polyarray[i] = this->mod_mul(this->polyarray[i] , this->R2modq);
        }
    }
    else{
        for(int i = 0;i < 256;i++){
            this->nttarray[i] = this->mod_mul(this->nttarray[i] , this->R2modq);
        }
    }
}
template <typename T, typename DT>
void Polynomial<T,DT>::rev_mont(){
    if(montflag){
        return ;
    }
    montflag = 0;
    if(nttflag==0){
        for(int i = 0;i < 256;i++){
            this->polyarray[i] = this->mod_mul(this->polyarray[i] , 1);
        }
    }
    else{
        for(int i = 0;i < 256;i++){
            this->nttarray[i] = this->mod_mul(this->nttarray[i] , 1);
        }
    }
}

template <typename T, typename DT>
void Polynomial<T, DT>::getpoly(T *reslist)
{
    if(this->nttflag){
        std::memcpy(reslist , this->nttarray , 256*sizeof(T));
    }
    else{
        std::memcpy(reslist , this->polyarray , 256*sizeof(T));
    }
}
template <typename T, typename DT>
T Polynomial<T,DT>::mod_mul(T a , T b){
    return montgomery_reduce<T , DT>((DT)a * b , this->qinv , this->q , this->Tbit);
}

template <typename T, typename DT>
T Polynomial<T, DT>::mod(T a)
{
    return simple_mod(a , this->q);
}

template class Polynomial<int16_t , int32_t>;
template class Polynomial<int32_t , int64_t>;