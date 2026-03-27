from math import *

for N in range(1, 100000)[::-1]:
    i = ceil(log2(N))
    L = 211
    I = ceil(L * i / 8)
    if 23_654*I <= 3241 * 2**10:
        print(N)
        break