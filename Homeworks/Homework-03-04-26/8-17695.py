from itertools import product
from string import printable as alph


cnt = 0
for val in product(alph[:7], repeat = 5):
    val = ''.join(val)
    if val[0] != '0' and sum(1 for x in val if int(x) in range(3, 6)) == 2:
        if sum(val[i] != val[i + 1] for i in range(len(val) - 1)) == 4:
            cnt += 1
print(cnt)