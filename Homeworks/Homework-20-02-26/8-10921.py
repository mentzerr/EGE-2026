from itertools import permutations

k = 0
for val in set(permutations('ДЖАВАСКРИПТ')):
    val = ''.join(val)
    s = 0
    for n in 'АИ':
        val = val.replace(n, '*')
    for pos, i in enumerate(val, start = 1):
        if i == '*':
            s += pos
    if s == 11:
        k += 1
print(k)
