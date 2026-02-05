def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0: return False
    return True

def f(num):
    d = set()
    for j in range(2, int(num ** .5) + 1):
        if num % j == 0:
            if is_prime(j): d |= {j}
            if is_prime(num // j): d |= {num // j}

    if len(d) > 1:
        return max(d) + min(d)
    return 0

k = 0
for N in range(5_400_001, 10**30):
    M = f(N)
    if M > 60000 and str(M) == str(M)[::-1]:
        print(N, M)
        k += 1
        if k == 5:
            break
