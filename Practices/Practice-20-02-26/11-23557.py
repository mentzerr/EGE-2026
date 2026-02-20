from math import *

for L in range(1, 10**9):
    N = 52 + 10 + 500
    i = ceil(log2(N))
    I = L * i / 8
    if I * 45_887 >= 49*2**20:
        print(L)
        break