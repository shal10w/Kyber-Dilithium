#ifndef POLYMAT_H
#define POLYMAT_H
#include "polyvec.h"

template <typename T , int k>
class polymat{
public:
    polyvec<T , k> *veclist[k];    
    polymat(polyvec<T,k> *veclist[]);
    void right_mul(polyvec<T , k>*res , polyvec<T,k> *rvalue);
    void trans();
    ~polymat();

};

#include "polymat_impl.h"

#endif

