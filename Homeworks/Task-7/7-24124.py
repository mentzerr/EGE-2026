from math import *

for t in range(1, 10000)[::-1]:
    VA_ZH = 2 * 48*10**3 * 24 * t
    if VA_ZH <= 20*2**23 * 1.4:
        print(t)
        break
