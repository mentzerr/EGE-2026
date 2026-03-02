from math import *

for I in range(1, 100000):
    VF = 2560*1440*I
    if VF * 52 >= 8388608 * 520:
        print(2**(I-1)+1)
        break