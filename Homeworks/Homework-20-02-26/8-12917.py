from itertools import permutations

k = 0
for val in set(permutations('ПРОСТО')):
    val = ''.join(val)
    if 'ОО' not in val:
        k += 1
print(k)
