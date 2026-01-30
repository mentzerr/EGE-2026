def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}

    for i in sorted(d):
        if i % 10 == 8 and i != 8:
            return i
    return 0

k = 0
for N in range(800_001, 10 ** 20):
    if F := f(N):
        print(N, F)
        k += 1
        if k == 5:
            break

