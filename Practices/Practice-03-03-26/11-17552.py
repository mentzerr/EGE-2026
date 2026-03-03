from math import *

for N in range(1, 10000):
    L = 261
    I = ceil(L * ceil(log2(N)) / 8)
    if I * 252_500 >= 31 * 2 ** 20:
        print(N)
        break