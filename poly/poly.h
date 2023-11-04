#ifndef POLY_H
#define POLY_H
#include <stdint.h>
#include <cstring>
template <typename T, typename DT>
class Polynomial{
public:
    T nttarray[256];
    T polyarray[256];
    T q,qinv,R2modq;
    int qbit , nttflag, montflag;
    Polynomial(T *array , int nttflag);
    void add(Polynomial *res , Polynomial *b);
    void sub(Polynomial *res , Polynomial *b);
    void to_mont();
    void rev_mont();
    T mod_mul(T a , T b);
    T mod(T a);
    void getpoly(T *reslist);
};

#endif