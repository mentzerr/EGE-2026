from itertools import permutations

k = 0
for val in set(permutations('ДЖАВАСКРИПТ')):
    val = ''.join(val)
    s = 0
    for pos, i in enumerate(val, start = 1):
        if i in 'АИ':
            s += pos
    if s == 11:
        k += 1
print(k)
