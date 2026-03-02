from math import *

for N in range(1, 10000):
    L = 248
    I = ceil(log2(N)) * L
    if 75_600 * I > 16 * 2 ** 23:
        print(N)
        break