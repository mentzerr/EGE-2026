from itertools import product
alph = sorted('СУЛАК')

for x in range(1, 10):
    for pos, val in enumerate(product(alph, repeat = x), start = 1):
        val = ''.join(val)
        if pos == 12368 and val[0] in 'ЛС' and val.count('У') + val.count("А") <= 2 and \
        'УА' not in val and 'АУ' not in val and 'УУ' not in val and 'АА' not in val:
            print(x)
            break
