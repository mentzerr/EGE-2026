from math import *

for L in range(1, 10000000):
    N = 10 + 26 + 8164
    I = ceil(ceil(log2(N)) * L / 8)
    if I * 835 > 156 * 2 ** 10:
        print(L)
        break