from itertools import permutations
alph = 'ТИХОРЕЦК'
k = 0
for val in permutations(alph, r = 4):
    val = ''.join(val)
    if val.count('И') + val.count('О') + val.count('Е') == 2:
        if sum(val[i] == 'ТИХО'[i] for i in range(4)) == 2:
            k += 1
print(k)