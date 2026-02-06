def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}

    if len(d) > 1:
        return sum(d) // len(d)
    return 0

k = 0
for N in range(1, 700_000)[::-1]:
    M = f(N)
    if str(M)[-3:] == '313':
        print(N, M)
        k += 1
        if k == 7:
            break