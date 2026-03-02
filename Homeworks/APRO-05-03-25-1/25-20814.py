def div(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            d |= {num // i, i}
    if len(d) > 1:
        return sum(d)
    return 0

k = 0
for N in range(500_001, 10**9):
    R = div(N)
    if str(R)[-1] == '9':
        print(N, R)
        k += 1
        if k == 5:
            break
