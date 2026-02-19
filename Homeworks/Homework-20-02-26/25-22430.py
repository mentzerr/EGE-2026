def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0: return False
    return True

def divisor(num):
    d = set()
    for j in range(2, int(num ** .5) + 1):
        if num % j == 0:
            if is_prime(j): d |= {j}
            if is_prime(num // j): d |= {num // j}

    if len(d) >= 4:
        d = sorted(d)
        return d[0] + d[1] + d[-1] + d[-2]
    return 0

k = 0
for N in range(456_790, 10**9):
    M = divisor(N)
    if M % 114 == 39:
        print(N, M)
        k += 1
        if k == 5:
            break
