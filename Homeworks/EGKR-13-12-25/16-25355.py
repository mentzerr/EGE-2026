from functools import lru_cache

@lru_cache(None)
def G(n):
    if n >= 248045: return n / 20 + 28
    return G(n + 9) - 4

def F(n):
    if n >= 19: return F(n - 4) + 3580
    return 6 * (G(n - 7) - 36)

for i in range(250_000, 1, -1):
    G(i)


print(F(673))