#include "../poly/Dilithiumpoly.h"
#include "../poly/poly.h"
#include <iostream>
#include "../poly/debug.h"
using namespace std;

int main(){
    int32_t a1[256] , a2[256];
    for(int i = 0 ; i < 256;i++){
        a1[i] = (142-2*i) % 8380417;
    }
    for(int i = 0 ; i < 256;i++){
        a2[i] = i;
    }
    DilithiumPoly *poly1 = new DilithiumPoly(a1 , 0 , 0);
    DilithiumPoly *poly2 = new DilithiumPoly(a2 , 0 , 0);
    DilithiumPoly *poly3 = new DilithiumPoly(0 , 1 , 1);
    poly1->to_ntt();
    poly2->to_ntt();
    poly3->mul(poly1 , poly2);
    cout << poly1->nttarray[0] << " " << poly2->nttarray[0] << " " << poly3->nttarray[0]<<endl;
    
    poly3->to_poly();
    output(poly3->polyarray , "1087312*x^2 + 1022492*x + 957440:");
    return 0;
}

