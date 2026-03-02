from math import *

for i in range(1, 1000):
    V_A = (11*60+20) * 1 * 32*10**3 * i
    if V_A * .7 >= 60*2**23:
        print(i)
        break