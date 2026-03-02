from math import *

for I in range(1, 10000)[::-1]:
    V = 96*10**3 * 2 * (3*60 + 33) * I
    if V * .6 <= 25 * 2**23:
        print(I)
        break