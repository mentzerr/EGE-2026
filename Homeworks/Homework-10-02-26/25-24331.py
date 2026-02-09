def fact(num):
    pm = []
    while num % 2 == 0:
        pm += [2]
        num //= 2

    i = 3
    while i**2 < num:
        while num % i == 0:
                pm += [i]
                num //= i
        i += 2

    if num > 2:
        pm += [num]

    if len(pm) == 5 and all('5' in str(d) for d in pm):
        return max(pm)
    return 0

k = 0
for N in range(13_475_125, 10**10):
    if Z := fact(N):
        print(N, Z)
        k += 1
        if k == 5:
            break

