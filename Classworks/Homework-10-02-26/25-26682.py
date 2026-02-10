def dell(num):
    d = set()
    for i in range(1, int(num ** .5) + 1):
        if num % i == 0:
            d |= {num // i, i}

    return d

def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2

    i = 3
    while i**2 <= num:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 1:
        d += [num]

    return d

k = 0
for N in range(5_200_000 + 1, 10**10):
    M = fact(N)
    D = dell(N)
    if len(M) == 9 and len(D) % 90 == 0:
        print(N, max(M))
        k += 1
        if k == 5:
            break
