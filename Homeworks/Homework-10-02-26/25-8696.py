def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    if is_prime(num): return 0
    d = set()
    for j in range(2, int(num ** .5) + 1):
        if num % j == 0:
            d |= {j, num // j}

    if len(d) > 1:
        return sum(d)
    return 0

k = 0
for N in range(1_273_548, 10**10):
    M = f(N)
    if is_prime(M % 100_000):
        print(N, M)
        k += 1
        if k == 5:
            break
