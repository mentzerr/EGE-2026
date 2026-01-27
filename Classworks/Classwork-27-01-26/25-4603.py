from fnmatch import fnmatch

for N in range(12347 - 12347 % 141, 10 ** 8 + 1, 141):
    if fnmatch(str(N), '1234*7') and N % 141 == 0:
        print(N, N // 141)

#######################################################
from itertools import product
from string import printable as alph

for l in range(0, 4):
    for Z in product(alph[:10], repeat = l):
        num = int('1234' + ''.join(Z) + '7')
        if num % 141 == 0:
            print(num, num // 141)

