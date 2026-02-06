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
for N in range(89_428_305, 10**20):
    D = fact(N)
    if len(D) >= 6 and N % sum(D) == 0:
        print(N, sum(D))
        k += 1
        if k == 6:
            break