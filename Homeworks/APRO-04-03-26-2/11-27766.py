from math import *

for L in range(1, 1000):
    N = 10 + 26 + 34
    I = ceil(L * ceil(log2(N)) / 8)
    if I * 1142 > 305 * 1024:
        print(L)
        break