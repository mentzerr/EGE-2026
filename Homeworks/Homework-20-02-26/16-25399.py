from functools import lru_cache

@lru_cache(None)
def G(n):
    if n > 303_728: return n - 15
    return G(n + 8) / 2 - 109

@lru_cache(None)
def F(n):
    if n >= 128: return F(n - 5) + 1092
    return 5 * G(n - 7) + 29

for i in range(310_000, 10, -1):
    G(i)

for i in range(127, 2100):
    F(i)

print(F(2049))