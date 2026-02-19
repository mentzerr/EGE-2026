from functools import lru_cache

@lru_cache(None)
def F(n):
    if n < 10: return n + 1
    return F(n - 8) + 2**n

for i in range(9, 4200):
    F(i)

print((F(4000) + 2 * F(3992)) / F(3984))