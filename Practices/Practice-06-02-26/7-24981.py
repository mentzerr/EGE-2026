from math import *
h = 1080
w = 1920
j1 = 60
j2 = 24
i1 = log(4096, 2)
i2 = log(2048, 2)
t = 57
print((h*w*i1*j1*t - h*w*i2*j2*t) / 2**13)
