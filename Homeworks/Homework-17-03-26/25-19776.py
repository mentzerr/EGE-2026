def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def div(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            if is_prime(i): d |= {i}
            if is_prime(num // i): d |= {num // i}

    if d:
        return max(d) + min(d)
    return 0

k = 0
for N in range(23_600_001, 10**10):
    if M := div(N):
        if M % 213 == 171:
            print(N, M)
            k += 1
            if k == 6:
                break
