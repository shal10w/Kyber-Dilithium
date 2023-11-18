#ifndef POLYVEC_H
#define POLYVEC_H

#include "../poly/poly.h"
#include "../poly/Dilithiumpoly.h"
#include "../poly/Kyberpoly.h"

template <typename T>
class polyvec{
public:
    T** datavec;
    int k;
    polyvec(T* vec[] , int k);
    void reset(int nttflag , int montflag);
    void mul(T*res , polyvec* rvalue);
    void add(polyvec *res , polyvec *rvalue);
    void to_poly();
    void to_ntt();
    ~polyvec();
};


#include "polyvec_impl.h"

#endif

