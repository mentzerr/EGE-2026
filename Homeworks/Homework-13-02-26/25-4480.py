from math import prod
def f(num):
    d = set()
    for i in range(1, int(num ** .5) + 1):
        if num % i == 0:
            d |= {num // i, i}

    if len(d) > 10 and sum(d) % 2 == prod(d) % 2 == 1:
        return len(d)
    return 0

k = 0
for N in range(800_000 + 1, 10**10):
    if D := f(N):
        print(N, D)
        k += 1
        if k == 6:
            break