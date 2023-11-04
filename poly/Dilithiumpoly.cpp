#include "Dilithiumpoly.h"
DilithiumPoly::DilithiumPoly(int32_t *array, int nttflag):Polynomial(array , nttflag){
    q = 8380417 , qinv = 8396801 , R2modq = 6273035;
    qbit = 24;
}


void DilithiumPoly::mul(DilithiumPoly *res, DilithiumPoly *b){
    for(int i = 0 ;i < 256 ; i++){
        res->nttarray[i] = mod_mul(this->nttarray[i] , b->nttarray[i]);
    }
}

void DilithiumPoly::to_poly()
{
}
/*
void DilithiumPoly::to_poly(){
    unsigned int start, len, j, k;
    int32_t t, zeta;
    k = 256;
    std::memcpy(polyarray , nttarray , 256*sizeof(int32_t));
    for(len = 1; len < 256; len <<= 1) {
        for(start = 0; start < 256; start = j + len) {
            zeta = -zetas[--k];
            for(j = start; j < start + len; ++j) {
                t = a[j];
                a[j] = t + a[j + len];
                a[j + len] = t - a[j + len];
                a[j + len] = mod_mul(zeta , a[j + len]);
            }
        }
    }
}
*/
void DilithiumPoly::to_ntt(){
    unsigned int len, start, j, k;
    int32_t zeta, t;
    k = 0;
    std::memcpy(nttarray , polyarray , 256*sizeof(int32_t));
    for(len = 128; len > 0; len >>= 1) {
        for(start = 0; start < 256; start = j + len){
            zeta = zetas[++k];
            for(j = start; j < start + len; ++j) {
                t = mod_mul(zeta , nttarray[j + len]);
                nttarray[j + len] = nttarray[j] - t;
                nttarray[j] = nttarray[j] + t;
            }
        }
    }
}
