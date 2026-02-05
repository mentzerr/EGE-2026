from math import prod
def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0: return False
    return True

def f(num):
    d = []
    for j in range(2, int(num ** .5) + 1):
        if num % j == 0:
            if is_prime(j): d += [j]
            if is_prime(num // j): d += [num // j]

    if len(d) == 12 and prod(d) == num:
        return max(d)
    return 0

k = 0
for N in range(24_517_513, 10**9):
    if F := f(N):
        print(N, F)
        k += 1
        if k == 5:
            break
