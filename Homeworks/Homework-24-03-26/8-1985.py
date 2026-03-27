from itertools import permutations

alph = 'АБИКОЛУН'

k = 0
for val in permutations(alph):
    val = ''.join(val)
    for i in 'АИОУ':
        val = val.replace(i, '*')
    for j in 'БКЛН':
        val = val.replace(j, '+')
    if '**' not in val and '++' not in val:
        k += 1
print(k)