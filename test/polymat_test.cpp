#include "../kernel/poly/Kyberpoly.h"
#include "../kernel/poly/poly.h"
#include "../kernel/vec/polyvec.h"
#include "../kernel/vec/polymat.h"
#include <iostream>
#include "../kernel/poly/debug.h"
using namespace std;

int main(){
    int16_t a1[256] , a2[256];
    KyberPoly *p1[2] , *p2[2];

    polyvec<KyberPoly,2> *pv1 , *pv2 ,*pv3, *res;
    polyvec<KyberPoly,2> *pvlist[2];
    polymat<KyberPoly,2> *pmat;
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
    pv1 = new polyvec<KyberPoly,2>(p1);
    pv2 = new polyvec<KyberPoly,2>(p2);
    pv3 = new polyvec<KyberPoly,2>(p1);
    res = new polyvec<KyberPoly,2>(NULL);
    pvlist[0] = pv1;
    pvlist[1] = pv2;
    pmat = new polymat<KyberPoly,2>(pvlist);
    // test right mul
    pmat->trans();
    pmat->trans();
    pmat->right_mul(res , pv1);
    res->to_poly();
    output(res->datavec[0]->polyarray , "should be 497*x^2 + 2822*x + 1482");
    output(res->datavec[1]->polyarray , "should be 497*x^2 + 2822*x + 1482");
    output(pv3->datavec[0]->nttarray , "pv1[0] ");
    output(pv3->datavec[1]->nttarray , "pv1[1] ");
    // test trans
    pmat->trans();
    res->reset(1,1);
    output(pv3->datavec[0]->nttarray , "pv1[0] ");
    output(pv3->datavec[1]->nttarray , "pv1[1] ");
    pmat->right_mul(res , pv3);
    res->to_poly();
    output(res->datavec[0]->polyarray , "should be 497*x^2 + 2822*x + 1482");
    output(res->datavec[1]->polyarray , "should be 497*x^2 + 2822*x + 1482");
    return 0;
}