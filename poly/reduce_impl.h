#include <iostream>

template <typename T,typename DT>
T montgomery_reduce(DT a , T Qinv , T Q, int Rbit){
    // R = 2^k
    DT t;
    T u;
    T R = (1 << Rbit) - 1;
    u = ((a&R)*Qinv) & R;
    std::cout << u << std::endl;
    t = (DT)u*Q;
    std::cout << t << std::endl;
    t = a - t;
    std::cout << t << std::endl;
    t >>= Rbit;
    std::cout << t << std::endl;
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
T mod_plus(T a , T b , T q){
    T res = a + b;
    if(res > q){
        return res - q;
    }
    return res;
}
template <typename T>
T mod_sub(T a , T b , T q){
    T res = a - b;
    if(res < 0){
        return res + q;
    }
    return res;
}