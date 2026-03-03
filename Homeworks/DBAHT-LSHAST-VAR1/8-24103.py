from itertools import product
alph = sorted('БУРАТИНО')

for pos, val in enumerate(product(alph, repeat = 5)):
    val = ''.join(val)
    if pos % 2 == 1 and len(set(val)) == 5:
        for i in 'УАИО':
            val = val.replace(i, '*')
            if val[0] != '*':
                print(pos)