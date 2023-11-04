#ifndef KYBERPOLY_H
#define KYBERPOLY_H
#include "poly.h"

class KyberPoly:Polynomial<int16_t , int32_t>{
public:
    const int16_t q = 3329 , qinv = 4865 , R2modq = 2882;
    const int qbit = 13;
    KyberPoly(int16_t *array , int nttflag);
    void mul(KyberPoly *res , KyberPoly *b);
    void to_poly();
    void to_ntt();
};
#endif