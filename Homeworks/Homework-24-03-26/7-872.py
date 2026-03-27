from math import *

for vol in range(1, 1000000):
    i = ceil(log2(256))
    V = 128 * 256 * i / 2**23
    num = 24 * 60 * 60 / 6
    if V * num <= vol:
        print(vol)
        break
