#include "./Dilithiumpoly.h"
DilithiumPoly::DilithiumPoly(int32_t *array, int nttflag,int montflag):
    Polynomial(array , nttflag , montflag){
    q = 8380417 , qinv = 58728449 , R2modq = 2365951;
    Tbit = 32;
}


void DilithiumPoly::mul(DilithiumPoly *a, DilithiumPoly *b){
    for(int i = 0 ;i < 256 ; i++){
        this->nttarray[i] = mod_mul(a->nttarray[i] , b->nttarray[i]);
    }
    nttflag = 1;
    montflag = 1;
}

void DilithiumPoly::to_poly(){
    unsigned int start, len, j, k;
    int32_t t, zeta;
    if(nttflag == 0){
        return ;
    }
    nttflag = 0;
    k = 256;
    std::memcpy(polyarray , nttarray , 256*sizeof(int32_t));
    if(montflag == 0){
        to_mont();
    }
    for(len = 1; len < 256; len <<= 1) {
        for(start = 0; start < 256; start += 2* len) {
            zeta = -dilithiumzetas[--k];
            for(j = start; j < start + len; ++j) {
                t = polyarray[j];
                polyarray[j] = mod(t + polyarray[j + len]);
                polyarray[j + len] = mod(t - polyarray[j + len]);
                polyarray[j + len] = mod_mul(zeta , polyarray[j + len]);
            }
        }
    }
    for(int i = 0;i<256;i++){
        polyarray[i] = mod_mul(polyarray[i] , 8347681);
    }
    montflag = 0;
}

void DilithiumPoly::to_ntt(){
    unsigned int len, start, j, k;
    int32_t zeta, t;
    if(nttflag){
        return;
    }
    nttflag = 1;
    
    k = 0;
    std::memcpy(nttarray , polyarray , 256*sizeof(int32_t));
    if(montflag == 0){
        to_mont();
    }
    for(len = 128; len > 0; len >>= 1) {
        for(start = 0; start < 256; start += 2*len){
            zeta = dilithiumzetas[++k];
            for(j = start; j < start + len; ++j) {
                t = mod_mul(zeta , nttarray[j + len]);
                nttarray[j + len] = mod(nttarray[j] - t);
                nttarray[j] = mod(nttarray[j] + t);
            }
        }
    }
}
