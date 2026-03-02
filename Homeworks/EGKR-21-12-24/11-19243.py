from math import *

for N in range(1, 10000):
    L = 377
    i = ceil(log2(N))
    I = ceil(5536 * 1024 / 23155)
    if i == ceil(I * 8 / L):
        print(N)
        break
