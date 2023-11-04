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
    
    int cnt2=0, cnt1=0 , cnt_2=0;
    int32_t temp;
    for(int i = 0;i<256;i++){
        temp = poly->nttarray[i];
        if(temp > 2*poly->q){
            cnt2++;
            cout << "larger than 2q! " << temp << "  " << temp/poly->q << endl;
            continue;
        }
        if(temp < -2*poly->q){
            cnt_2++;
            cout << "smaller than -2q! " << temp << "  " << temp/poly->q << endl;
            continue;
        }
    }
    cout << cnt2 << "  " << cnt_2 << endl;
    return 0;
}

