from itertools import product

alph = sorted('МАСЛО')

k = 0
for val in product(alph, repeat = 6):
    val = ''.join(val)
    for i in 'АО':
        val = val.replace(i, '*')
    for j in 'МСЛ':
        val = val.replace(j, '+')
    if val.count('*') == 1 and val.count('+') <= 6:
        k += 1
print(k)