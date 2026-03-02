from math import *

for pac in range(1, 10000)[::-1]:
    VF = 1024*960*ceil(log2(16_384)) / 2**23
    if VF * 400 >= pac:
        print(pac)
        break