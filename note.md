## reduce


### Montgomery reduction

输入a，计算$aR^{-1} \mod{q}$。
R的取值为$2^k$，k为q的位数，计算时，需要预计算$q^{-1} \mod{R}$，由此能够得到$a - aq^{-1}q \mod{R} = 0$，从而$aR^{-1} = \frac{a - (aq^{-1} \mod{R})q}{R}$ 

### Barrett reduce

输入a,计算$a \mod{q}$
取$m = [2^{2k}/q]$,k为q的bit数,则$am>>2k \approx a/q$. $a - (am>>2k)q = [a/q - a/2^{2k}] \in [-2q , 2q]$,还需要进一步约至[0,q]
### NTT

#### Dilithium

$r = 1753 , r^512 = 1 \mod{q}$ , $rlist[i] = r^{2i+1} \mod{q}$