from math import *

for N in range(1, 100000)[::-1]:
    VF = 1024*960*ceil(log2(N))
    if VF * 32 / 1_474_560 < 140:
        print(N)
        break
