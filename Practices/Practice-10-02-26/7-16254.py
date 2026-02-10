from math import *
Vs = 3 * 2 **23
hw = 1600*1200
n = 1024
i_c = ceil(log2(n))
vi = 1.2 * Vs
i = floor(vi / hw)
print(2**(i - i_c))
