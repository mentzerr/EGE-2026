from math import *

for A in range(1, 10000)[::-1]:
    VF = A*768*ceil(log2(4000))
    if VF * 50 <= 1_310_720 * 300:
        print(A)
        break