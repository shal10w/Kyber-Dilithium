#include "Kyberpoly.h"
#include "debug.h"
KyberPoly::KyberPoly(int16_t *array, int nttflag , int montflag):
    Polynomial(array , nttflag , montflag){
    q = 3329 , qinv = 62209 , R2modq = 1353;
    Tbit = 16;
}

void KyberPoly::mul(KyberPoly *a, KyberPoly *b){
    int16_t a1 , a2 , b1 , b2 , zeta;
    for(int i = 0 ; i < 128;i++){
        zeta = kyberzetas[64+(i>>1)];
        if(i&1 == 1){
            zeta = -zeta;
        }
        a1 = a->nttarray[i*2];
        a2 = a->nttarray[i*2+1];
        b1 = b->nttarray[i*2];
        b2 = b->nttarray[i*2+1];
        this->nttarray[i*2] = mod(mod_mul(mod_mul(a2 , b2) , zeta) + mod_mul(a1,b1));
        this->nttarray[i*2+1] = mod(mod_mul(a1 , b2) + mod_mul(a2 , b1));
    }
}

void KyberPoly::to_poly(){
    if(nttflag == 0){
        return ;
    }
    nttflag = 0;
    std::memcpy(polyarray , nttarray , 256*sizeof(int16_t));
    if(montflag == 0){
        to_mont();
    }
    unsigned int start, len, j, k;
    int16_t t, zeta;
    k = 128;
    for(len = 2; len < 256; len <<= 1) {
        for(start = 0; start < 256; start += 2* len) {
            zeta = -kyberzetas[--k];
            for(j = start; j < start + len; ++j) {
                t = polyarray[j];
                polyarray[j] = mod(t + polyarray[j + len]);
                polyarray[j + len] = mod(t - polyarray[j + len]);
                polyarray[j + len] = mod_mul(zeta , polyarray[j + len]);
            }
        }
    }
    for(int i = 0;i<128;i++){
        polyarray[i] = mod_mul(polyarray[i] , 3303); // inverse(128 , 3329)
    }
    montflag = 0;
}

void KyberPoly::to_ntt(){
    if(nttflag == 1){
        return ;
    }
    nttflag = 1;
    std::memcpy(nttarray , polyarray , 256*sizeof(int16_t));
    if(montflag == 0){
        to_mont();
    }
    int len, start, j, k;
    int16_t t, zeta;

    k = 1;
    for(len = 128; len >= 2; len >>= 1) {
        for(start = 0; start < 256; start += 2 * len) {
            zeta = kyberzetas[k++];
            for(j = start; j < start + len; ++j) {
            t = mod_mul(zeta, nttarray[j + len]);
            nttarray[j + len] = mod(nttarray[j] - t);
            nttarray[j] = mod(nttarray[j] + t);
            }
        }
    }
}
