from itertools import product
from string import printable as alph
k = 0
for val in product(alph[:9], repeat = 7):
    val = ''.join(val)
    if val[0] != '0' and val.count('8') == 1 and val[0] not in '1357' and val[-1] not in '02468':
        k += 1
print(k)