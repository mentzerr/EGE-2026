def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            if i % 2 == 1: d |= {i}
            if num // i % 2 == 1: d |= {num // i}
    if len(d) == 3:
            return d
    return {}

k = 0
for N in range(18782, 18823):
    if F := f(N):
        print(*sorted(F))
