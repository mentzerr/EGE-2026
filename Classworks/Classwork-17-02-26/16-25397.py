from functools import lru_cache

@lru_cache(None)
def G(n):
    if n >= 301208: return 10*n + 50
    return G(n + 7) - 21

def F(n):
    if n > 40: return F(n - 4) + 3020
    return 3 * (G(n - 2) - 15)

for i in range(301208, 0, -1):
    G(i)

print(F(2026))

