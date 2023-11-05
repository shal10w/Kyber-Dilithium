from sage.all import *

PR = PolynomialRing(Zmod(8380417) , "x")
x = PR.gens()[0]
a1 = 0
for i in range(256):
    a1 += (142-2*i) * x**i

a2 = 0
for i in range(256):
    a2 += i*x**i

print((a1 * a2)%(x**256+1))

#7488257*x^255 + 7610657*x^254 + 7731813*x^253 + 7851729*x^252 + 7970409*x^251 + 8087857*x^250 + 8204077*x^249 + 8319073*x^248 + 52432*x^247 + 164992*x^246 + 276340*x^245 + 386480*x^244 + 495416*x^243 + 603152*x^242 + 709692*x^241 + 815040*x^240 + 919200*x^239 + 1022176*x^238 + 1123972*x^237 + 1224592*x^236 + 1324040*x^235 + 1422320*x^234 + 1519436*x^233 + 1615392*x^232 + 1710192*x^231 + 1803840*x^230 + 1896340*x^229 + 1987696*x^228 + 2077912*x^227 + 2166992*x^226 + 2254940*x^225 + 2341760*x^224 + 2427456*x^223 + 2512032*x^222 + 2595492*x^221 + 2677840*x^220 + 2759080*x^219 + 2839216*x^218 + 2918252*x^217 + 2996192*x^216 + 3073040*x^215 + 3148800*x^214 + 3223476*x^213 + 3297072*x^212 + 3369592*x^211 + 3441040*x^210 + 3511420*x^209 + 3580736*x^208 + 3648992*x^207 + 3716192*x^206 + 3782340*x^205 + 3847440*x^204 + 3911496*x^203 + 3974512*x^202 + 4036492*x^201 + 4097440*x^200 + 4157360*x^199 + 4216256*x^198 + 4274132*x^197 + 4330992*x^196 + 4386840*x^195 + 4441680*x^194 + 4495516*x^193 + 4548352*x^192 + 4600192*x^191 + 4651040*x^190 + 4700900*x^189 + 4749776*x^188 + 4797672*x^187 + 4844592*x^186 + 4890540*x^185 + 4935520*x^184 + 4979536*x^183 + 5022592*x^182 + 5064692*x^181 + 5105840*x^180 + 5146040*x^179 + 5185296*x^178 + 5223612*x^177 + 5260992*x^176 + 5297440*x^175 + 5332960*x^174 + 5367556*x^173 + 5401232*x^172 + 5433992*x^171 + 5465840*x^170 + 5496780*x^169 + 5526816*x^168 + 5555952*x^167 + 5584192*x^166 + 5611540*x^165 + 5638000*x^164 + 5663576*x^163 + 5688272*x^162 + 5712092*x^161 + 5735040*x^160 + 5757120*x^159 + 5778336*x^158 + 5798692*x^157 + 5818192*x^156 + 5836840*x^155 + 5854640*x^154 + 5871596*x^153 + 5887712*x^152 + 5902992*x^151 + 5917440*x^150 + 5931060*x^149 + 5943856*x^148 + 5955832*x^147 + 5966992*x^146 + 5977340*x^145 + 5986880*x^144 + 5995616*x^143 + 6003552*x^142 + 6010692*x^141 + 6017040*x^140 + 6022600*x^139 + 6027376*x^138 + 6031372*x^137 + 6034592*x^136 + 6037040*x^135 + 6038720*x^134 + 6039636*x^133 + 6039792*x^132 + 6039192*x^131 + 6037840*x^130 + 6035740*x^129 + 6032896*x^128 + 6029312*x^127 + 6024992*x^126 + 6019940*x^125 + 6014160*x^124 + 6007656*x^123 + 6000432*x^122 + 5992492*x^121 + 5983840*x^120 + 5974480*x^119 + 5964416*x^118 + 5953652*x^117 + 5942192*x^116 + 5930040*x^115 + 5917200*x^114 + 5903676*x^113 + 5889472*x^112 + 5874592*x^111 + 5859040*x^110 + 5842820*x^109 + 5825936*x^108 + 5808392*x^107 + 5790192*x^106 + 5771340*x^105 + 5751840*x^104 + 5731696*x^103 + 5710912*x^102 + 5689492*x^101 + 5667440*x^100 + 5644760*x^99 + 5621456*x^98 + 5597532*x^97 + 5572992*x^96 + 5547840*x^95 + 5522080*x^94 + 5495716*x^93 + 5468752*x^92 + 5441192*x^91 + 5413040*x^90 + 5384300*x^89 + 5354976*x^88 + 5325072*x^87 + 5294592*x^86 + 5263540*x^85 + 5231920*x^84 + 5199736*x^83 + 5166992*x^82 + 5133692*x^81 + 5099840*x^80 + 5065440*x^79 + 5030496*x^78 + 4995012*x^77 + 4958992*x^76 + 4922440*x^75 + 4885360*x^74 + 4847756*x^73 + 4809632*x^72 + 4770992*x^71 + 4731840*x^70 + 4692180*x^69 + 4652016*x^68 + 4611352*x^67 + 4570192*x^66 + 4528540*x^65 + 4486400*x^64 + 4443776*x^63 + 4400672*x^62 + 4357092*x^61 + 4313040*x^60 + 4268520*x^59 + 4223536*x^58 + 4178092*x^57 + 4132192*x^56 + 4085840*x^55 + 4039040*x^54 + 3991796*x^53 + 3944112*x^52 + 3895992*x^51 + 3847440*x^50 + 3798460*x^49 + 3749056*x^48 + 3699232*x^47 + 3648992*x^46 + 3598340*x^45 + 3547280*x^44 + 3495816*x^43 + 3443952*x^42 + 3391692*x^41 + 3339040*x^40 + 3286000*x^39 + 3232576*x^38 + 3178772*x^37 + 3124592*x^36 + 3070040*x^35 + 3015120*x^34 + 2959836*x^33 + 2904192*x^32 + 2848192*x^31 + 2791840*x^30 + 2735140*x^29 + 2678096*x^28 + 2620712*x^27 + 2562992*x^26 + 2504940*x^25 + 2446560*x^24 + 2387856*x^23 + 2328832*x^22 + 2269492*x^21 + 2209840*x^20 + 2149880*x^19 + 2089616*x^18 + 2029052*x^17 + 1968192*x^16 + 1907040*x^15 + 1845600*x^14 + 1783876*x^13 + 1721872*x^12 + 1659592*x^11 + 1597040*x^10 + 1534220*x^9 + 1471136*x^8 + 1407792*x^7 + 1344192*x^6 + 1280340*x^5 + 1216240*x^4 + 1151896*x^3 + 1087312*x^2 + 1022492*x + 957440