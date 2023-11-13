#include "../poly/poly.h"
#include "../poly/Dilithiumpoly.h"
#include "../poly/Kyberpoly.h"

template <typename T , int k>
class polyvec{
public:
    T* datavec[k];
    polyvec(T* vec[]);
    void mul(T*res , polyvec* rvalue);
    ~polyvec();
};


#include "polyvec_impl.h"