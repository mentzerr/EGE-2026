from itertools import product

alph = sorted('КРАТЕ')

for pos, val in enumerate(product(alph, repeat = 6), start = 1):
    val = ''.join(val)
    if val == 'РАКЕТА':
        s = pos
    if val == 'КАРЕТА':
        j = pos
print(s - j - 1)