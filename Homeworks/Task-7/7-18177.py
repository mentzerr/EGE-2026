from math import *

for t in range(1, 100000)[::-1]:
    sound = 96*10**3 * 24 * (75*60 + 45) * 1
    song = sound / 2**13 + 256
    if song * 2**13 >= 209_715_200 * t:
        print(t)
        break
