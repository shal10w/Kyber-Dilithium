#include "../poly/kyberpoly.h"
#include "../poly/poly.h"
#include <iostream>
#include "../poly/debug.h"
using namespace std;

int main(){
    int16_t a1[256] , a2[256];
    for(int i = 0 ; i < 256;i++){
        a1[i] = (142-2*i) % 3329;
    }
    for(int i = 0 ; i < 256;i++){
        a2[i] = i;
    }
    KyberPoly *poly1 = new KyberPoly(a1 , 0 , 0);
    poly1->to_mont();
    output(poly1->polyarray , "polyarray: ");
    poly1->to_ntt();
    
    output(poly1->nttarray , "nttarray: ");
    poly1->to_poly();

    output(poly1->polyarray , "polyarray: ");
    return 0;
}

