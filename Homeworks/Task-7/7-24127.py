from math import *

for pict in range(1, 100000)[::-1]:
    VS = 4096*8192*24 / 2**13
    VS_ZH = VS - VS * .35 + 64
    if VS_ZH * pict < 5 * 2**20:
        print(pict)
        break
