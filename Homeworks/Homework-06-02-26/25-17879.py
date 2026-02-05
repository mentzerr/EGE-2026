def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}

    if len(d) > 1:
        return min(d) + max(d)
    return 0

k = 0
for N in range (800_001, 10**10):
    M = f(N)
    if M % 10 == 4:
        print(N, M)
        k += 1
        if k == 5:
            break