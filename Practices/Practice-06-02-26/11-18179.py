from math import *
l = 20
io = ceil(11*2**20 / 600_000)
i = io * 8 / l
print(2**(i-1)+1)