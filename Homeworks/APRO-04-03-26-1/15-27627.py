def DEL(n, m):
    return n % m == 0

def f(x):
    return DEL(x, 25) <= ((not DEL(x, A)) <= (not DEL(x, 60)))

for A in range(1, 10000)[::-1]:
    if all(f(x) for x in range(1, 10000)):
        print(A)
        break