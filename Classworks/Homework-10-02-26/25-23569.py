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
for N in range(6_086_055 + 1, 10**10):
    M = fact(N)
    if len(M) == 2 and all(str(i).count('6') == 1 for i in M):
                print(N, max(M))
                k += 1
                if k == 5:
                    break






