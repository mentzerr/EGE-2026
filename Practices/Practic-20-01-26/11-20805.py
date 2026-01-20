from math import *
l = 248
ib = ceil(16*1024*1024 / 75600)
i = ceil(ib * 8 / l)
print(2**(i-1)+1)
