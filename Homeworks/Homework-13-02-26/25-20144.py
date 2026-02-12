def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0: return False
    return True

def div(num):
    d = set()
    for j in range(2, int(num ** .5) + 1):
        if num % j == 0:
            if is_prime(j): d |= {j}
            if is_prime(num // j): d |= {num // j}

    if len(d) > 1:
        return max(d) - min(d)
    return 0

k = 0
for N in range(3_333_337 + 1, 10**10):
    R = div(N)
    if R > 1000 and R % 3 == 0:
        print(N, R)
        k += 1
        if k == 5:
            break