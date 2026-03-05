from math import *

for i in range(1, 1000)[::-1]:
    VF = 192*960*i
    VF_ZH = .85 * VF
    if VF_ZH < 90 * 2**13:
        print(2**i)
        break