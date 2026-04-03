def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num * .5) + 1):
        if num % i == 0: return False
    return True

def div(num):
    d = set()

    for j in range(2, int(num * .5) + 1):
        if num % j == 0:
            if is_prime(j): d |= {j}
            if is_prime(num // j): d |= {num // j}

    if len(d) == 3:
        return max(d)
    return 0

cnt = 0
for N in range(1_000_001, 10**10):
    if D := div(N):
        print(N, D)
        cnt += 1
        if cnt == 5:
            break
            