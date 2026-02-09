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

    if len(d) == 4 and str(sum(map(int, d))) == str(sum(map(int, d)))[::-1]:
        return sum(d)
    return 0

k = 0
for N in range(7_305_659, 10**10):
    if F := fact(N):
        print(N, F)
        k += 1
        if k == 5:
            break



