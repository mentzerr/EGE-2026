from itertools import permutations
from string import printable as alph

k = 0
for val in permutations(alph[:8], r = 5):
    val = ''.join(val)
    if val[0] != '0' and '1' not in val:
        for i in alph[:8:2]:
            val = val.replace(i, '+')
        for j in alph[1:8:2]:
            val = val.replace(j, '*')
        if '++' not in val and '**' not in val:
            k += 1
print(k)
