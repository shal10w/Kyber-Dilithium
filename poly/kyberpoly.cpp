#include "kyberpoly.h"


KyberPoly::KyberPoly(int16_t *array, int nttflag , int montflag):
    Polynomial(array , nttflag , montflag){}

void KyberPoly::mul(KyberPoly *res, KyberPoly *b){

}

void KyberPoly::to_poly()
{
}

void KyberPoly::to_ntt()
{
}
