from sage.all import *
#test kyber
PR = PolynomialRing(Zmod(3329) , "x")

#test dilithium
#PR = PolynomialRing(Zmod(8380417) , "x")

x = PR.gens()[0]
a1 = 0
for i in range(256):
    a1 += (142-2*i) * x**i

a2 = 0
for i in range(256):
    a2 += i*x**i



#dilithium test
print((a1 * a2)%(x**256+1))
#7488257*x^255 + 7610657*x^254 + 7731813*x^253 + 7851729*x^252 + 7970409*x^251 + 8087857*x^250 + 8204077*x^249 + 8319073*x^248 + 52432*x^247 + 164992*x^246 + 276340*x^245 + 386480*x^244 + 495416*x^243 + 603152*x^242 + 709692*x^241 + 815040*x^240 + 919200*x^239 + 1022176*x^238 + 1123972*x^237 + 1224592*x^236 + 1324040*x^235 + 1422320*x^234 + 1519436*x^233 + 1615392*x^232 + 1710192*x^231 + 1803840*x^230 + 1896340*x^229 + 1987696*x^228 + 2077912*x^227 + 2166992*x^226 + 2254940*x^225 + 2341760*x^224 + 2427456*x^223 + 2512032*x^222 + 2595492*x^221 + 2677840*x^220 + 2759080*x^219 + 2839216*x^218 + 2918252*x^217 + 2996192*x^216 + 3073040*x^215 + 3148800*x^214 + 3223476*x^213 + 3297072*x^212 + 3369592*x^211 + 3441040*x^210 + 3511420*x^209 + 3580736*x^208 + 3648992*x^207 + 3716192*x^206 + 3782340*x^205 + 3847440*x^204 + 3911496*x^203 + 3974512*x^202 + 4036492*x^201 + 4097440*x^200 + 4157360*x^199 + 4216256*x^198 + 4274132*x^197 + 4330992*x^196 + 4386840*x^195 + 4441680*x^194 + 4495516*x^193 + 4548352*x^192 + 4600192*x^191 + 4651040*x^190 + 4700900*x^189 + 4749776*x^188 + 4797672*x^187 + 4844592*x^186 + 4890540*x^185 + 4935520*x^184 + 4979536*x^183 + 5022592*x^182 + 5064692*x^181 + 5105840*x^180 + 5146040*x^179 + 5185296*x^178 + 5223612*x^177 + 5260992*x^176 + 5297440*x^175 + 5332960*x^174 + 5367556*x^173 + 5401232*x^172 + 5433992*x^171 + 5465840*x^170 + 5496780*x^169 + 5526816*x^168 + 5555952*x^167 + 5584192*x^166 + 5611540*x^165 + 5638000*x^164 + 5663576*x^163 + 5688272*x^162 + 5712092*x^161 + 5735040*x^160 + 5757120*x^159 + 5778336*x^158 + 5798692*x^157 + 5818192*x^156 + 5836840*x^155 + 5854640*x^154 + 5871596*x^153 + 5887712*x^152 + 5902992*x^151 + 5917440*x^150 + 5931060*x^149 + 5943856*x^148 + 5955832*x^147 + 5966992*x^146 + 5977340*x^145 + 5986880*x^144 + 5995616*x^143 + 6003552*x^142 + 6010692*x^141 + 6017040*x^140 + 6022600*x^139 + 6027376*x^138 + 6031372*x^137 + 6034592*x^136 + 6037040*x^135 + 6038720*x^134 + 6039636*x^133 + 6039792*x^132 + 6039192*x^131 + 6037840*x^130 + 6035740*x^129 + 6032896*x^128 + 6029312*x^127 + 6024992*x^126 + 6019940*x^125 + 6014160*x^124 + 6007656*x^123 + 6000432*x^122 + 5992492*x^121 + 5983840*x^120 + 5974480*x^119 + 5964416*x^118 + 5953652*x^117 + 5942192*x^116 + 5930040*x^115 + 5917200*x^114 + 5903676*x^113 + 5889472*x^112 + 5874592*x^111 + 5859040*x^110 + 5842820*x^109 + 5825936*x^108 + 5808392*x^107 + 5790192*x^106 + 5771340*x^105 + 5751840*x^104 + 5731696*x^103 + 5710912*x^102 + 5689492*x^101 + 5667440*x^100 + 5644760*x^99 + 5621456*x^98 + 5597532*x^97 + 5572992*x^96 + 5547840*x^95 + 5522080*x^94 + 5495716*x^93 + 5468752*x^92 + 5441192*x^91 + 5413040*x^90 + 5384300*x^89 + 5354976*x^88 + 5325072*x^87 + 5294592*x^86 + 5263540*x^85 + 5231920*x^84 + 5199736*x^83 + 5166992*x^82 + 5133692*x^81 + 5099840*x^80 + 5065440*x^79 + 5030496*x^78 + 4995012*x^77 + 4958992*x^76 + 4922440*x^75 + 4885360*x^74 + 4847756*x^73 + 4809632*x^72 + 4770992*x^71 + 4731840*x^70 + 4692180*x^69 + 4652016*x^68 + 4611352*x^67 + 4570192*x^66 + 4528540*x^65 + 4486400*x^64 + 4443776*x^63 + 4400672*x^62 + 4357092*x^61 + 4313040*x^60 + 4268520*x^59 + 4223536*x^58 + 4178092*x^57 + 4132192*x^56 + 4085840*x^55 + 4039040*x^54 + 3991796*x^53 + 3944112*x^52 + 3895992*x^51 + 3847440*x^50 + 3798460*x^49 + 3749056*x^48 + 3699232*x^47 + 3648992*x^46 + 3598340*x^45 + 3547280*x^44 + 3495816*x^43 + 3443952*x^42 + 3391692*x^41 + 3339040*x^40 + 3286000*x^39 + 3232576*x^38 + 3178772*x^37 + 3124592*x^36 + 3070040*x^35 + 3015120*x^34 + 2959836*x^33 + 2904192*x^32 + 2848192*x^31 + 2791840*x^30 + 2735140*x^29 + 2678096*x^28 + 2620712*x^27 + 2562992*x^26 + 2504940*x^25 + 2446560*x^24 + 2387856*x^23 + 2328832*x^22 + 2269492*x^21 + 2209840*x^20 + 2149880*x^19 + 2089616*x^18 + 2029052*x^17 + 1968192*x^16 + 1907040*x^15 + 1845600*x^14 + 1783876*x^13 + 1721872*x^12 + 1659592*x^11 + 1597040*x^10 + 1534220*x^9 + 1471136*x^8 + 1407792*x^7 + 1344192*x^6 + 1280340*x^5 + 1216240*x^4 + 1151896*x^3 + 1087312*x^2 + 1022492*x + 9574400

#kyber test
#12*x^255 + 2568*x^254 + 551*x^253 + 623*x^252 + 2788*x^251 + 392*x^250 + 97*x^249 + 1907*x^248 + 2497*x^247 + 1871*x^246 + 33*x^245 + 316*x^244 + 2724*x^243 + 603*x^242 + 615*x^241 + 2764*x^240 + 396*x^239 + 173*x^238 + 2099*x^237 + 2849*x^236 + 2427*x^235 + 837*x^234 + 1412*x^233 + 827*x^232 + 2415*x^231 + 2851*x^230 + 2139*x^229 + 283*x^228 + 616*x^227 + 3142*x^226 + 1207*x^225 + 1473*x^224 + 615*x^223 + 1966*x^222 + 2201*x^221 + 1324*x^220 + 2668*x^219 + 2908*x^218 + 2048*x^217 + 92*x^216 + 373*x^215 + 2895*x^214 + 1004*x^213 + 1362*x^212 + 644*x^211 + 2183*x^210 + 2654*x^209 + 2061*x^208 + 408*x^207 + 1028*x^206 + 596*x^205 + 2445*x^204 + 3250*x^203 + 3015*x^202 + 1744*x^201 + 2770*x^200 + 2768*x^199 + 1742*x^198 + 3025*x^197 + 3292*x^196 + 2547*x^195 + 794*x^194 + 1366*x^193 + 938*x^192 + 2843*x^191 + 427*x^190 + 352*x^189 + 2622*x^188 + 583*x^187 + 897*x^186 + 239*x^185 + 1942*x^184 + 2681*x^183 + 2460*x^182 + 1283*x^181 + 2483*x^180 + 2735*x^179 + 2043*x^178 + 411*x^177 + 1172*x^176 + 1001*x^175 + 3231*x^174 + 1208*x^173 + 1594*x^172 + 1064*x^171 + 2951*x^170 + 601*x^169 + 676*x^168 + 3180*x^167 + 1459*x^166 + 2175*x^165 + 2003*x^164 + 947*x^163 + 2340*x^162 + 2857*x^161 + 2502*x^160 + 1279*x^159 + 2521*x^158 + 2903*x^157 + 2429*x^156 + 1103*x^155 + 2258*x^154 + 2569*x^153 + 2040*x^152 + 675*x^151 + 1807*x^150 + 2111*x^149 + 1591*x^148 + 251*x^147 + 1424*x^146 + 1785*x^145 + 1338*x^144 + 87*x^143 + 1365*x^142 + 1847*x^141 + 1537*x^140 + 439*x^139 + 1886*x^138 + 2553*x^137 + 2444*x^136 + 1563*x^135 + 3243*x^134 + 830*x^133 + 986*x^132 + 386*x^131 + 2363*x^130 + 263*x^129 + 748*x^128 + 493*x^127 + 2831*x^126 + 1108*x^125 + 1986*x^124 + 2140*x^123 + 1574*x^122 + 292*x^121 + 1627*x^120 + 2254*x^119 + 2177*x^118 + 1400*x^117 + 3256*x^116 + 1091*x^115 + 1567*x^114 + 1359*x^113 + 471*x^112 + 2236*x^111 + 425*x^109 + 186*x^108 + 2616*x^107 + 1061*x^106 + 2183*x^105 + 2657*x^104 + 2487*x^103 + 1677*x^102 + 231*x^101 + 1482*x^100 + 2105*x^99 + 2104*x^98 + 1483*x^97 + 246*x^96 + 1726*x^95 + 2598*x^94 + 2866*x^93 + 2534*x^92 + 1606*x^91 + 86*x^90 + 1307*x^89 + 1944*x^88 + 2001*x^87 + 1482*x^86 + 391*x^85 + 2061*x^84 + 3167*x^83 + 384*x^82 + 374*x^81 + 3141*x^80 + 2031*x^79 + 377*x^78 + 1512*x^77 + 2111*x^76 + 2178*x^75 + 1717*x^74 + 732*x^73 + 2556*x^72 + 535*x^71 + 1331*x^70 + 1619*x^69 + 1403*x^68 + 687*x^67 + 2804*x^66 + 1100*x^65 + 2237*x^64 + 2890*x^63 + 3063*x^62 + 2760*x^61 + 1985*x^60 + 742*x^59 + 2364*x^58 + 197*x^57 + 903*x^56 + 1157*x^55 + 963*x^54 + 325*x^53 + 2576*x^52 + 1062*x^51 + 2445*x^50 + 71*x^49 + 602*x^48 + 713*x^47 + 408*x^46 + 3020*x^45 + 1895*x^44 + 366*x^43 + 1766*x^42 + 2770*x^41 + 53*x^40 + 277*x^39 + 117*x^38 + 2906*x^37 + 1990*x^36 + 702*x^35 + 2375*x^34 + 355*x^33 + 1304*x^32 + 1897*x^31 + 2138*x^30 + 2031*x^29 + 1580*x^28 + 789*x^27 + 2991*x^26 + 1532*x^25 + 3074*x^24 + 963*x^23 + 1861*x^22 + 2443*x^21 + 2713*x^20 + 2675*x^19 + 2333*x^18 + 1691*x^17 + 753*x^16 + 2852*x^15 + 1334*x^14 + 2861*x^13 + 779*x^12 + 1750*x^11 + 2449*x^10 + 2880*x^9 + 3047*x^8 + 2954*x^7 + 2605*x^6 + 2004*x^5 + 1155*x^4 + 62*x^3 + 2058*x^2 + 489*x + 2017

#polyvec test1
#print((2*a1*a2)%(x**256+1))
#24*x^255 + 1807*x^254 + 1102*x^253 + 1246*x^252 + 2247*x^251 + 784*x^250 + 194*x^249 + 485*x^248 + 1665*x^247 + 413*x^246 + 66*x^245 + 632*x^244 + 2119*x^243 + 1206*x^242 + 1230*x^241 + 2199*x^240 + 792*x^239 + 346*x^238 + 869*x^237 + 2369*x^236 + 1525*x^235 + 1674*x^234 + 2824*x^233 + 1654*x^232 + 1501*x^231 + 2373*x^230 + 949*x^229 + 566*x^228 + 1232*x^227 + 2955*x^226 + 2414*x^225 + 2946*x^224 + 1230*x^223 + 603*x^222 + 1073*x^221 + 2648*x^220 + 2007*x^219 + 2487*x^218 + 767*x^217 + 184*x^216 + 746*x^215 + 2461*x^214 + 2008*x^213 + 2724*x^212 + 1288*x^211 + 1037*x^210 + 1979*x^209 + 793*x^208 + 816*x^207 + 2056*x^206 + 1192*x^205 + 1561*x^204 + 3171*x^203 + 2701*x^202 + 159*x^201 + 2211*x^200 + 2207*x^199 + 155*x^198 + 2721*x^197 + 3255*x^196 + 1765*x^195 + 1588*x^194 + 2732*x^193 + 1876*x^192 + 2357*x^191 + 854*x^190 + 704*x^189 + 1915*x^188 + 1166*x^187 + 1794*x^186 + 478*x^185 + 555*x^184 + 2033*x^183 + 1591*x^182 + 2566*x^181 + 1637*x^180 + 2141*x^179 + 757*x^178 + 822*x^177 + 2344*x^176 + 2002*x^175 + 3133*x^174 + 2416*x^173 + 3188*x^172 + 2128*x^171 + 2573*x^170 + 1202*x^169 + 1352*x^168 + 3031*x^167 + 2918*x^166 + 1021*x^165 + 677*x^164 + 1894*x^163 + 1351*x^162 + 2385*x^161 + 1675*x^160 + 2558*x^159 + 1713*x^158 + 2477*x^157 + 1529*x^156 + 2206*x^155 + 1187*x^154 + 1809*x^153 + 751*x^152 + 1350*x^151 + 285*x^150 + 893*x^149 + 3182*x^148 + 502*x^147 + 2848*x^146 + 241*x^145 + 2676*x^144 + 174*x^143 + 2730*x^142 + 365*x^141 + 3074*x^140 + 878*x^139 + 443*x^138 + 1777*x^137 + 1559*x^136 + 3126*x^135 + 3157*x^134 + 1660*x^133 + 1972*x^132 + 772*x^131 + 1397*x^130 + 526*x^129 + 1496*x^128 + 986*x^127 + 2333*x^126 + 2216*x^125 + 643*x^124 + 951*x^123 + 3148*x^122 + 584*x^121 + 3254*x^120 + 1179*x^119 + 1025*x^118 + 2800*x^117 + 3183*x^116 + 2182*x^115 + 3134*x^114 + 2718*x^113 + 942*x^112 + 1143*x^111 + 850*x^109 + 372*x^108 + 1903*x^107 + 2122*x^106 + 1037*x^105 + 1985*x^104 + 1645*x^103 + 25*x^102 + 462*x^101 + 2964*x^100 + 881*x^99 + 879*x^98 + 2966*x^97 + 492*x^96 + 123*x^95 + 1867*x^94 + 2403*x^93 + 1739*x^92 + 3212*x^91 + 172*x^90 + 2614*x^89 + 559*x^88 + 673*x^87 + 2964*x^86 + 782*x^85 + 793*x^84 + 3005*x^83 + 768*x^82 + 748*x^81 + 2953*x^80 + 733*x^79 + 754*x^78 + 3024*x^77 + 893*x^76 + 1027*x^75 + 105*x^74 + 1464*x^73 + 1783*x^72 + 1070*x^71 + 2662*x^70 + 3238*x^69 + 2806*x^68 + 1374*x^67 + 2279*x^66 + 2200*x^65 + 1145*x^64 + 2451*x^63 + 2797*x^62 + 2191*x^61 + 641*x^60 + 1484*x^59 + 1399*x^58 + 394*x^57 + 1806*x^56 + 2314*x^55 + 1926*x^54 + 650*x^53 + 1823*x^52 + 2124*x^51 + 1561*x^50 + 142*x^49 + 1204*x^48 + 1426*x^47 + 816*x^46 + 2711*x^45 + 461*x^44 + 732*x^43 + 203*x^42 + 2211*x^41 + 106*x^40 + 554*x^39 + 234*x^38 + 2483*x^37 + 651*x^36 + 1404*x^35 + 1421*x^34 + 710*x^33 + 2608*x^32 + 465*x^31 + 947*x^30 + 733*x^29 + 3160*x^28 + 1578*x^27 + 2653*x^26 + 3064*x^25 + 2819*x^24 + 1926*x^23 + 393*x^22 + 1557*x^21 + 2097*x^20 + 2021*x^19 + 1337*x^18 + 53*x^17 + 1506*x^16 + 2375*x^15 + 2668*x^14 + 2393*x^13 + 1558*x^12 + 171*x^11 + 1569*x^10 + 2431*x^9 + 2765*x^8 + 2579*x^7 + 1881*x^6 + 679*x^5 + 2310*x^4 + 124*x^3 + 787*x^2 + 978*x + 705

#polyvec test2
#print((a1+a2)%(x**256+1))
#3216*x^255 + 3217*x^254 + 3218*x^253 + 3219*x^252 + 3220*x^251 + 3221*x^250 + 3222*x^249 + 3223*x^248 + 3224*x^247 + 3225*x^246 + 3226*x^245 + 3227*x^244 + 3228*x^243 + 3229*x^242 + 3230*x^241 + 3231*x^240 + 3232*x^239 + 3233*x^238 + 3234*x^237 + 3235*x^236 + 3236*x^235 + 3237*x^234 + 3238*x^233 + 3239*x^232 + 3240*x^231 + 3241*x^230 + 3242*x^229 + 3243*x^228 + 3244*x^227 + 3245*x^226 + 3246*x^225 + 3247*x^224 + 3248*x^223 + 3249*x^222 + 3250*x^221 + 3251*x^220 + 3252*x^219 + 3253*x^218 + 3254*x^217 + 3255*x^216 + 3256*x^215 + 3257*x^214 + 3258*x^213 + 3259*x^212 + 3260*x^211 + 3261*x^210 + 3262*x^209 + 3263*x^208 + 3264*x^207 + 3265*x^206 + 3266*x^205 + 3267*x^204 + 3268*x^203 + 3269*x^202 + 3270*x^201 + 3271*x^200 + 3272*x^199 + 3273*x^198 + 3274*x^197 + 3275*x^196 + 3276*x^195 + 3277*x^194 + 3278*x^193 + 3279*x^192 + 3280*x^191 + 3281*x^190 + 3282*x^189 + 3283*x^188 + 3284*x^187 + 3285*x^186 + 3286*x^185 + 3287*x^184 + 3288*x^183 + 3289*x^182 + 3290*x^181 + 3291*x^180 + 3292*x^179 + 3293*x^178 + 3294*x^177 + 3295*x^176 + 3296*x^175 + 3297*x^174 + 3298*x^173 + 3299*x^172 + 3300*x^171 + 3301*x^170 + 3302*x^169 + 3303*x^168 + 3304*x^167 + 3305*x^166 + 3306*x^165 + 3307*x^164 + 3308*x^163 + 3309*x^162 + 3310*x^161 + 3311*x^160 + 3312*x^159 + 3313*x^158 + 3314*x^157 + 3315*x^156 + 3316*x^155 + 3317*x^154 + 3318*x^153 + 3319*x^152 + 3320*x^151 + 3321*x^150 + 3322*x^149 + 3323*x^148 + 3324*x^147 + 3325*x^146 + 3326*x^145 + 3327*x^144 + 3328*x^143 + x^141 + 2*x^140 + 3*x^139 + 4*x^138 + 5*x^137 + 6*x^136 + 7*x^135 + 8*x^134 + 9*x^133 + 10*x^132 + 11*x^131 + 12*x^130 + 13*x^129 + 14*x^128 + 15*x^127 + 16*x^126 + 17*x^125 + 18*x^124 + 19*x^123 + 20*x^122 + 21*x^121 + 22*x^120 + 23*x^119 + 24*x^118 + 25*x^117 + 26*x^116 + 27*x^115 + 28*x^114 + 29*x^113 + 30*x^112 + 31*x^111 + 32*x^110 + 33*x^109 + 34*x^108 + 35*x^107 + 36*x^106 + 37*x^105 + 38*x^104 + 39*x^103 + 40*x^102 + 41*x^101 + 42*x^100 + 43*x^99 + 44*x^98 + 45*x^97 + 46*x^96 + 47*x^95 + 48*x^94 + 49*x^93 + 50*x^92 + 51*x^91 + 52*x^90 + 53*x^89 + 54*x^88 + 55*x^87 + 56*x^86 + 57*x^85 + 58*x^84 + 59*x^83 + 60*x^82 + 61*x^81 + 62*x^80 + 63*x^79 + 64*x^78 + 65*x^77 + 66*x^76 + 67*x^75 + 68*x^74 + 69*x^73 + 70*x^72 + 71*x^71 + 72*x^70 + 73*x^69 + 74*x^68 + 75*x^67 + 76*x^66 + 77*x^65 + 78*x^64 + 79*x^63 + 80*x^62 + 81*x^61 + 82*x^60 + 83*x^59 + 84*x^58 + 85*x^57 + 86*x^56 + 87*x^55 + 88*x^54 + 89*x^53 + 90*x^52 + 91*x^51 + 92*x^50 + 93*x^49 + 94*x^48 + 95*x^47 + 96*x^46 + 97*x^45 + 98*x^44 + 99*x^43 + 100*x^42 + 101*x^41 + 102*x^40 + 103*x^39 + 104*x^38 + 105*x^37 + 106*x^36 + 107*x^35 + 108*x^34 + 109*x^33 + 110*x^32 + 111*x^31 + 112*x^30 + 113*x^29 + 114*x^28 + 115*x^27 + 116*x^26 + 117*x^25 + 118*x^24 + 119*x^23 + 120*x^22 + 121*x^21 + 122*x^20 + 123*x^19 + 124*x^18 + 125*x^17 + 126*x^16 + 127*x^15 + 128*x^14 + 129*x^13 + 130*x^12 + 131*x^11 + 132*x^10 + 133*x^9 + 134*x^8 + 135*x^7 + 136*x^6 + 137*x^5 + 138*x^4 + 139*x^3 + 140*x^2 + 141*x + 142

#polymat test1
#print((2*a1*a1)%(x**256+1))
#372*x^255 + 2761*x^254 + 2332*x^253 + 2398*x^252 + 2943*x^251 + 622*x^250 + 2077*x^249 + 634*x^248 + 2935*x^247 + 2306*x^246 + 2060*x^245 + 2181*x^244 + 2653*x^243 + 131*x^242 + 1257*x^241 + 2686*x^240 + 1073*x^239 + 3060*x^238 + 1973*x^237 + 1125*x^236 + 500*x^235 + 82*x^234 + 3184*x^233 + 3132*x^232 + 3239*x^231 + 160*x^230 + 537*x^229 + 1025*x^228 + 1608*x^227 + 2270*x^226 + 2995*x^225 + 438*x^224 + 1241*x^223 + 2059*x^222 + 2876*x^221 + 347*x^220 + 1114*x^219 + 1832*x^218 + 2485*x^217 + 3057*x^216 + 203*x^215 + 565*x^214 + 798*x^213 + 886*x^212 + 813*x^211 + 563*x^210 + 120*x^209 + 2797*x^208 + 1920*x^207 + 802*x^206 + 2756*x^205 + 1108*x^204 + 2500*x^203 + 258*x^202 + 1024*x^201 + 1453*x^200 + 1529*x^199 + 1236*x^198 + 558*x^197 + 2808*x^196 + 1312*x^195 + 2712*x^194 + 334*x^193 + 820*x^192 + 825*x^191 + 333*x^190 + 2657*x^189 + 1123*x^188 + 2373*x^187 + 3062*x^186 + 3174*x^185 + 2693*x^184 + 1603*x^183 + 3217*x^182 + 861*x^181 + 1177*x^180 + 820*x^179 + 3103*x^178 + 1352*x^177 + 2209*x^176 + 2329*x^175 + 1696*x^174 + 294*x^173 + 1436*x^172 + 1777*x^171 + 1301*x^170 + 3321*x^169 + 1163*x^168 + 1469*x^167 + 894*x^166 + 2751*x^165 + 366*x^164 + 381*x^163 + 2780*x^162 + 889*x^161 + 1350*x^160 + 818*x^159 + 2606*x^158 + 40*x^157 + 3091*x^156 + 1756*x^155 + 2677*x^154 + 2509*x^153 + 1236*x^152 + 2171*x^151 + 1969*x^150 + 614*x^149 + 1419*x^148 + 1039*x^147 + 2787*x^146 + 3318*x^145 + 2616*x^144 + 665*x^143 + 778*x^142 + 2939*x^141 + 474*x^140 + 25*x^139 + 1576*x^138 + 1782*x^137 + 627*x^136 + 1424*x^135 + 828*x^134 + 2152*x^133 + 2051*x^132 + 509*x^131 + 839*x^130 + 3025*x^129 + 393*x^128 + 2914*x^127 + 585*x^126 + 48*x^125 + 1287*x^124 + 957*x^123 + 2371*x^122 + 2184*x^121 + 380*x^120 + 272*x^119 + 1844*x^118 + 1751*x^117 + 3306*x^116 + 3164*x^115 + 1309*x^114 + 1054*x^113 + 2383*x^112 + 1951*x^111 + 3071*x^110 + 2398*x^109 + 3245*x^108 + 2267*x^107 + 2777*x^106 + 1430*x^105 + 1539*x^104 + 3088*x^103 + 2732*x^102 + 455*x^101 + 2899*x^100 + 61*x^99 + 1912*x^98 + 1778*x^97 + 2972*x^96 + 2149*x^95 + 2622*x^94 + 1046*x^93 + 734*x^92 + 1670*x^91 + 509*x^90 + 564*x^89 + 1819*x^88 + 929*x^87 + 1207*x^86 + 2637*x^85 + 1874*x^84 + 2231*x^83 + 363*x^82 + 2912*x^81 + 3204*x^80 + 1223*x^79 + 282*x^78 + 365*x^77 + 1456*x^76 + 210*x^75 + 3269*x^74 + 630*x^73 + 2264*x^72 + 1497*x^71 + 1642*x^70 + 2683*x^69 + 1275*x^68 + 731*x^67 + 1035*x^66 + 2171*x^65 + 794*x^64 + 217*x^63 + 424*x^62 + 1399*x^61 + 3126*x^60 + 2260*x^59 + 2114*x^58 + 2672*x^57 + 589*x^56 + 2507*x^55 + 1752*x^54 + 1637*x^53 + 2146*x^52 + 3263*x^51 + 1643*x^50 + 599*x^49 + 115*x^48 + 175*x^47 + 763*x^46 + 1863*x^45 + 130*x^44 + 2206*x^43 + 1417*x^42 + 1076*x^41 + 1167*x^40 + 1674*x^39 + 2581*x^38 + 543*x^37 + 2202*x^36 + 884*x^35 + 3231*x^34 + 2569*x^33 + 2211*x^32 + 2141*x^31 + 2343*x^30 + 2801*x^29 + 170*x^28 + 1092*x^27 + 2222*x^26 + 215*x^25 + 1713*x^24 + 42*x^23 + 1844*x^22 + 445*x^21 + 2487*x^20 + 1296*x^19 + 185*x^18 + 2467*x^17 + 1468*x^16 + 501*x^15 + 2879*x^14 + 1928*x^13 + 961*x^12 + 3291*x^11 + 2244*x^10 + 1133*x^9 + 3271*x^8 + 1984*x^7 + 585*x^6 + 2387*x^5 + 716*x^4 + 2214*x^3 + 207*x^2 + 1337*x + 2259

#polymat test2
#print((a1*a1+a1*a2)%(x**256+1))
#198*x^255 + 2284*x^254 + 1717*x^253 + 1822*x^252 + 2595*x^251 + 703*x^250 + 2800*x^249 + 2224*x^248 + 2300*x^247 + 3024*x^246 + 1063*x^245 + 3071*x^244 + 2386*x^243 + 2333*x^242 + 2908*x^241 + 778*x^240 + 2597*x^239 + 1703*x^238 + 1421*x^237 + 1747*x^236 + 2677*x^235 + 878*x^234 + 3004*x^233 + 2393*x^232 + 2370*x^231 + 2931*x^230 + 743*x^229 + 2460*x^228 + 1420*x^227 + 948*x^226 + 1040*x^225 + 1692*x^224 + 2900*x^223 + 1331*x^222 + 310*x^221 + 3162*x^220 + 3225*x^219 + 495*x^218 + 1626*x^217 + 3285*x^216 + 2139*x^215 + 1513*x^214 + 1403*x^213 + 1805*x^212 + 2715*x^211 + 800*x^210 + 2714*x^209 + 1795*x^208 + 1368*x^207 + 1429*x^206 + 1974*x^205 + 2999*x^204 + 1171*x^203 + 3144*x^202 + 2256*x^201 + 1832*x^200 + 1868*x^199 + 2360*x^198 + 3304*x^197 + 1367*x^196 + 3203*x^195 + 2150*x^194 + 1533*x^193 + 1348*x^192 + 1591*x^191 + 2258*x^190 + 16*x^189 + 1519*x^188 + 105*x^187 + 2428*x^186 + 1826*x^185 + 1624*x^184 + 1818*x^183 + 2404*x^182 + 49*x^181 + 1407*x^180 + 3145*x^179 + 1930*x^178 + 1087*x^177 + 612*x^176 + 501*x^175 + 750*x^174 + 1355*x^173 + 2312*x^172 + 288*x^171 + 1937*x^170 + 597*x^169 + 2922*x^168 + 2250*x^167 + 1906*x^166 + 1886*x^165 + 2186*x^164 + 2802*x^163 + 401*x^162 + 1637*x^161 + 3177*x^160 + 1688*x^159 + 495*x^158 + 2923*x^157 + 2310*x^156 + 1981*x^155 + 1932*x^154 + 2159*x^153 + 2658*x^152 + 96*x^151 + 1127*x^150 + 2418*x^149 + 636*x^148 + 2435*x^147 + 1153*x^146 + 115*x^145 + 2646*x^144 + 2084*x^143 + 1754*x^142 + 1652*x^141 + 1774*x^140 + 2116*x^139 + 2674*x^138 + 115*x^137 + 1093*x^136 + 2275*x^135 + 328*x^134 + 1906*x^133 + 347*x^132 + 2305*x^131 + 1118*x^130 + 111*x^129 + 2609*x^128 + 1950*x^127 + 1459*x^126 + 1132*x^125 + 965*x^124 + 954*x^123 + 1095*x^122 + 1384*x^121 + 1817*x^120 + 2390*x^119 + 3099*x^118 + 611*x^117 + 1580*x^116 + 2673*x^115 + 557*x^114 + 1886*x^113 + 3327*x^112 + 1547*x^111 + 3200*x^110 + 1624*x^109 + 144*x^108 + 2085*x^107 + 785*x^106 + 2898*x^105 + 1762*x^104 + 702*x^103 + 3043*x^102 + 2123*x^101 + 1267*x^100 + 471*x^99 + 3060*x^98 + 2372*x^97 + 1732*x^96 + 1136*x^95 + 580*x^94 + 60*x^93 + 2901*x^92 + 2441*x^91 + 2005*x^90 + 1589*x^89 + 1189*x^88 + 801*x^87 + 421*x^86 + 45*x^85 + 2998*x^84 + 2618*x^83 + 2230*x^82 + 1830*x^81 + 1414*x^80 + 978*x^79 + 518*x^78 + 30*x^77 + 2839*x^76 + 2283*x^75 + 1687*x^74 + 1047*x^73 + 359*x^72 + 2948*x^71 + 2152*x^70 + 1296*x^69 + 376*x^68 + 2717*x^67 + 1657*x^66 + 521*x^65 + 2634*x^64 + 1334*x^63 + 3275*x^62 + 1795*x^61 + 219*x^60 + 1872*x^59 + 92*x^58 + 1533*x^57 + 2862*x^56 + 746*x^55 + 1839*x^54 + 2808*x^53 + 320*x^52 + 1029*x^51 + 1602*x^50 + 2035*x^49 + 2324*x^48 + 2465*x^47 + 2454*x^46 + 2287*x^45 + 1960*x^44 + 1469*x^43 + 810*x^42 + 3308*x^41 + 2301*x^40 + 1114*x^39 + 3072*x^38 + 1513*x^37 + 3091*x^36 + 1144*x^35 + 2326*x^34 + 3304*x^33 + 745*x^32 + 1303*x^31 + 1645*x^30 + 1767*x^29 + 1665*x^28 + 1335*x^27 + 773*x^26 + 3304*x^25 + 2266*x^24 + 984*x^23 + 2783*x^22 + 1001*x^21 + 2292*x^20 + 3323*x^19 + 761*x^18 + 1260*x^17 + 1487*x^16 + 1438*x^15 + 1109*x^14 + 496*x^13 + 2924*x^12 + 1731*x^11 + 242*x^10 + 1782*x^9 + 3018*x^8 + 617*x^7 + 1233*x^6 + 1533*x^5 + 1513*x^4 + 1169*x^3 + 497*x^2 + 2822*x + 1482