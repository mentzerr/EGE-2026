from functools import lru_cache

@lru_cache(None)
def G(n):
    if n >= 30_000: return 3
    return G(n + 3) + 7

def F(n):
    return G(n + 1)

for i in range(33_000, 1490, -1):
    G(i)

print(F(1500))