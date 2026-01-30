def DEL(n, m):
    return n % m == 0

def f(x):
    return (DEL(405, x) <= DEL(81, x)) or (A - x > 162)

for A in range(1, 10000):
    if all(f(x) for x in range(1, 10000)):
        print(A)
        break