def prime(num):
    if num == 1: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0: return False
    return True

def f(num):
    d = set()
    for j in range(2, int(num ** .5) + 1):
        if num % j == 0:
            if prime(j): d |= {j}
            if prime(num // j): d |= {num // j}

    if len(d) > 1:
        return sum(d)
    return 0

k = 0
for N in range(32_500_000, 10**15):
    S = f(N)
    if S != 0 and S % 145 == 0:
        print(N, S)
        k += 1
        if k == 7:
            break

