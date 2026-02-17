from functools import lru_cache

@lru_cache(None)
def G(n):
    if n >= 221337: return 2 * n + 50
    return G(n + 11) - 48

@lru_cache(None)
def F(n):
    if n > 30: return F(n - 6) + 2048
    return 3 * (G(n - 5) + 13)

for i in range(221338, 0, -1):
    G(i)

for i in range(29, 221338):
    F(i)

print(F(5078))