from math import *

for L in range(1, 1000000):
    N = 10 + 52 + 454
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if I * 31_922 > 2 * 2**30:
        print(L)
        break