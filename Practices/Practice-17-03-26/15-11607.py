def DEL(n, m):
    return n % m == 0

def F(x):
    return (not(DEL(x, 263)) <= DEL(x, A)) and DEL(x, 71)

for A in range(1, 10000000):
    if all(F(x) == 0 for x in range(1, 10000000)):
        print(A)
