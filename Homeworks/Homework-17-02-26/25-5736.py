def div(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {num // i, i}

    if len(d) > 1:
        return max(d)
    return 0

k = 0
for N in range(10 ** 9 + 1, 10 ** 20):
    if str(N) == str(N)[::-1]:
        D = div(N)
        if D % 7 == 0:
            print(N, D)
            k += 1
            if k == 5:
                break
