def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2

    i = 3
    while i**2 < num:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 2:
        d += [num]
    return d

k = 0
for N in range(24_517_513, 10**20):
    D = fact(N)
    if len(D) == 12:
        print(N, max(D))
        k += 1
        if k == 5:
            break
            