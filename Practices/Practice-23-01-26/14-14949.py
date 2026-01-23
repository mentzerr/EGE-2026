from string import printable as alph
from math import log
for x in alph[1:8]:
    num1 = int(f'{x}1{x}', 16)
    num2 = int(f'{x}3{x}3', 8)
    num = num1 + num2
    if log(num, 2) % 1 == 0:
        print(x)

