#include "../kernel/poly/Kyberpoly.h"
#include "../kernel/poly/poly.h"
#include "../kernel/vec/polyvec.h"
#include <iostream>
#include "../kernel/poly/debug.h"
using namespace std;

int main(){
    int16_t a1[256] , a2[256];
    KyberPoly *p1[2] , *p2[2];
    KyberPoly *res;
    polyvec<KyberPoly,2> *pv1 , *pv2 , *addres;
    for(int i = 0 ; i < 256;i++){
        a1[i] = (142-2*i) % 3329;
    }
    for(int i = 0 ; i < 256;i++){
        a2[i] = i;
    }
    for(int i = 0;i<2;i++){
        p1[i] = new KyberPoly(a1 , 0 , 0);
        p2[i] = new KyberPoly(a2 , 0 , 0);
    }
    res = new KyberPoly(NULL , 1 , 1);
    pv1 = new polyvec<KyberPoly,2>(p1);
    output(pv1->datavec[0]->polyarray , "pv1->datavec0 ");
    pv2 = new polyvec<KyberPoly,2>(p2);
    addres = new polyvec<KyberPoly,2>(NULL);
    pv1->mul(res , pv2);
    res->to_poly();
    output(res->polyarray , "should be 787*x^2 + 978*x + 705");

    // test add
    pv1->add(addres , pv2);
    addres->to_poly();
    output(addres->datavec[0]->polyarray , "should be 140*x^2 + 141*x + 142");
    output(addres->datavec[1]->polyarray , "should be 140*x^2 + 141*x + 142");
}