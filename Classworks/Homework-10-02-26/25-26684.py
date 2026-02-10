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
for N in range(5_000_012, 10**10, 100):
    M = fact(N)
    if any(M.count(i) == 5 for i in set(M)):
        print(N, min(i for i in set(M) if M.count(i) == 5))
        k += 1
        if k == 5:
            break


