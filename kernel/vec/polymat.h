#ifndef POLYMAT_H
#define POLYMAT_H
#include "polyvec.h"

template <typename T>
class polymat{
public:
    polyvec<T> **veclist;
    int k; 
    polymat(polyvec<T> *veclist[] , int k);
    void right_mul(polyvec<T>*res , polyvec<T> *rvalue);
    void trans();
    ~polymat();

};

#include "polymat_impl.h"

#endif

