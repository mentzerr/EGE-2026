from math import *

for pic in range(1, 10000)[::-1]:
    VF = 1280*960*ceil(log2(2048))
    if VF * pic / 96_468_992 <= 132:
        print(pic)
        break