def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}

    if len(d) >= 7:
        return sorted(d)[-7], len(d)
    return ()

k = 0
for N in range(400_000_001, 10**20):
    if D := f(N):
        print(*D)
        k += 1
        if k == 5:
            break