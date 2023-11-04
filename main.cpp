#include "poly/Dilithiumpoly.h"
#include "poly/poly.h"
#include <iostream>
using namespace std;

int main(){
    DilithiumPoly *poly = new DilithiumPoly(NULL , 1);
    int32_t a = 8123123 , b = 8999999;

    cout << poly->mod_mul(a , b) << endl;
    return 0;
}

