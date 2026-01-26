def DEL(n,m):
    return n % m == 0

def f(x):
    B = x in range(80, 101)
    return DEL(x, 17) <= ((not B) or (A < x + 30))

for A in range(1, 1000)[::-1]:
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break
        