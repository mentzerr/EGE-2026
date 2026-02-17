from itertools import product

alph = sorted('СДАЙЕГЭ')

summ = 0
for pos, val in enumerate(product(alph, repeat = 6), start = 1):
    val = ''.join(val)
    if 'ЕГЭ' in val:
        summ += pos
print(summ)
