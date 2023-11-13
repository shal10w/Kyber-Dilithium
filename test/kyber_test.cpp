#include "../kernel/poly/Kyberpoly.h"
#include "../kernel/poly/poly.h"
#include <iostream>
#include "../kernel/poly/debug.h"
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
    KyberPoly *poly2 = new KyberPoly(a2 , 0 , 0);
    KyberPoly *poly3 = new KyberPoly(0 , 1 , 1);
    poly1->to_ntt();
    poly2->to_ntt();
    poly3->mul(poly1 , poly2);
    
    poly3->to_poly();
    output(poly3->polyarray , "2058*x^2 + 489*x + 2017:");
    return 0;
}

