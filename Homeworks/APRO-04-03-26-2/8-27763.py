from itertools import product

k = 0
for val in set(product('0123456', repeat = 5)):
    val = ''.join(val)
    if val[0] != '0' and val.count('0') == 1 and val.count('1') <= 2:
        k += 1
print(k)