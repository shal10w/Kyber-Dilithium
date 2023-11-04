#include "poly/Dilithiumpoly.h"
#include "poly/poly.h"
#include <iostream>
using namespace std;

int main(){
    int32_t a[256];
    for(int i = 0 ; i < 256;i++){
        a[i] = (i*114351) % 8380417;
    }
    DilithiumPoly *poly = new DilithiumPoly(a , 0);
    
    poly->to_ntt();
    poly->to_poly();
    for(int i = 0 ; i < 10;i++){
        cout << (i*114351) % 8380417 << " " << poly->polyarray[i] << endl;
    }
    return 0;
}

