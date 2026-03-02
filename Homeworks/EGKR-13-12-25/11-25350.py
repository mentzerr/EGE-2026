from math import *

for N in range(1, 10000):
    L = 105
    i = ceil(log2(N))
    I = L * i
    if I * 65_536 >= 7 * 2**23:
        print(N)
        break