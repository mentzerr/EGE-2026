from itertools import product

alph = sorted('АРГУМЕНТ')

for pos, val in enumerate(product(alph, repeat = 4), start = 1):
    val = ''.join(val)
    if len(val) == len(set(val)) and list(val) == sorted(val):
        print(pos)
