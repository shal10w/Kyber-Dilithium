#ifndef REDUCE_H
#define REDUCE_H

template <typename T,typename DT>T montgomery_reduce(DT a , T Qinv , T Q, int Rbit);
template <typename T,typename DT>T barrett_reduce(T a ,T q, T m , int kbit);

template <typename T>T simple_mod(T a , T q);
#include "reduce_impl.h"
#endif