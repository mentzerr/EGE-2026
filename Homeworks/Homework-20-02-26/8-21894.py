from itertools import permutations

k = 0

for val in permutations('0123456789', r = 4):
    val = ''.join(val)
    if val[0] != '0':
        for i in '02468':
            val = val.replace(i, '*')
        for j in '13579':
            val = val.replace(j, '+')
        if '**' not in val and '++' not in val:
            k += 1
print(k)