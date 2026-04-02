from itertools import product
from string import printable as alph

cnt = 0
for val in product(alph[:25], repeat = 4):
    val = ''.join(val)
    if val[0] != '0':
        if sum(int(x, 25) > 15 for x in val) > 2 and \
            sum(int(x, 25) % 2 == 0 for x in val) >= 1:
            cnt += 1
print(cnt)