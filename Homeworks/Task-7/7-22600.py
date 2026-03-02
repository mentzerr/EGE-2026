from math import *
for HW in range(1, 10000000)[::-1]:
    i = ceil(log2(10_000_000))
    if HW * i * 10 <= 2_100_000 * 180:
        print(HW)
        break