def f(num):
    d = {1}
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}

    if len(d) > 1:
        return sum(d) // len(d)
    return 0

k = 0
for N in range(1, 770_000)[::-1]:
    A = f(N)
    if A % 100 == 12:
        print(N, A)
        k += 1
        if k == 5:
            break