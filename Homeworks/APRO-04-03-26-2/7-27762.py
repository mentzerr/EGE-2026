from math import *

for t in range(1, 1000000):
    GS = 180 * 2 * 8 * 24_000
    if GS <= 48_000 * t:
        print(t)
        break