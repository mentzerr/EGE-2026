from functools import lru_cache

@lru_cache(None)
def G(n):
    if n < 100: return n
    return F(n - 3) + 1

def F(n):
    return G(n-2)

for i in range(1, 5000):
    G(i)

print(F(5000))