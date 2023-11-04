#ifndef REDUCE_H
#define REDUCE_H

template <typename T,typename DT>T montgomery_reduce(DT a , T Qinv , T Q, int Rbit);
template <typename T,typename DT>T barrett_reduce(T a ,T q, T m , int kbit);

template <typename T>T mod_plus(T a , T b , T q);
template <typename T>T mod_sub(T a , T b , T q);

#include "reduce_impl.h"
#endif