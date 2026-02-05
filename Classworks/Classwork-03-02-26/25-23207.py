def is_prime(num):
    for i in range(2, int(num ** .5) + 1):
        if num < 2: return False
        if num % i == 0:
            return False
    return True

def f(num):
    d = []
    for j in range(2, int(num ** .5) + 1):
        if num % j == 0:
            if is_prime(j) and str(j).count('5') == 1: d += [j]
            if is_prime(num // j) and str(num // j).count('5') == 1: d += [num // j]

    if len(d) == 2 and d[0] * d[1] == num:
        return max(d)
    return 0

k = 0
for N in range(1_324_728, 10**30):
    if F := f(N):
        print(N, F)
        k += 1
        if k == 5:
            break
