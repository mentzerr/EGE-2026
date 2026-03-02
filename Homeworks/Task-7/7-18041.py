from math import *

for i in range(1, 100000)[::-1]:
    V = 3840 * 2160 * i
    if V / 25_600 < 2*60**2:
        print(2**(floor(i / 8) * 8))
        break

