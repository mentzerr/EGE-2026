def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0: return False
    return True

def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            if is_prime(i): d |= {i}
            if is_prime(num // i): d |= {num // i}

    if len(d) > 1:
        M = min(d) + max(d)
        return M
    return 0

k = 0
for N in range(1_200_001, 10**20):
    M = f(N)
    if M > 2000 and M % 10 == 8:
        print(N, M)
        k += 1
        if k == 5:
            break
