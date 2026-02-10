from math import *
hw = 1024*768
i = floor(540*1024*8 / hw)
i_n = ceil(i / .65)
print(2**i_n)
