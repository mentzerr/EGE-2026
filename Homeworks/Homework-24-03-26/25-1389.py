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

    if len(d) > 0:
        return sum(d)
    return 0

k = 0
for N in range(250_001, 10 ** 9):
    S = divisor(N)
    if S % 17 == 0 and S != 0:
        print(N, S)
        k += 1
        if k == 5:
            break