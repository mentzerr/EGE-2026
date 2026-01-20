def DEL(n, m):
    return n % m == 0

def f(x):
    for x in range(1, 1000):
        B = x in range(50, 71)
        z = DEL(x, A) or (DEL(x, 23) <= (not B))
        if not z:
            return False
    return True

for A in range(1, 1000)[::-1]:
    if f(A):
        print(A)
        break
