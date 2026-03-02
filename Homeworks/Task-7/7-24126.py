from math import *

V_F_1 = 1280*3750*16
Q_1 = 12_800_000
T_1 = V_F_1 / Q_1


V_F_2 = 1200*800*log2(4096)
Q_2 = 320_000
T_2 = V_F_2 / Q_2

print(abs(T_1 - T_2))
