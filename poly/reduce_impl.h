#include <iostream>

template <typename T,typename DT>
T montgomery_reduce(DT a , T Qinv , T Q , int Tbit){
    // R = 2^k
    DT t;
    T u;
    u = a*Qinv;
    t = (DT)u*Q;
    t = a - t;
    t >>= Tbit;
    return (T)t;
}

template <typename T,typename DT>
T barrett_reduce(T a ,T q, T m , int kbit){
    // m/2^kbit = 1/q , kbit = 2qbit+2
    DT t;
    t = m*a >> kbit;
    t *= q;
    a -= t;
    return a;
}
template <typename T>
T simple_mod(T a , T q){
    if(a > q){
        return a - q;
    }
    if(a < -q){
        return a + q;
    }
    return a;
}