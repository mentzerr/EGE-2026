from math import *

for N in range(1, 10000):
    L = 119
    I = ceil(ceil(log2(N)) * L / 8)
    if I * 125_300 > 23 * 2 ** 20:
        print(N)
        break
print(int('1010111111', 2))