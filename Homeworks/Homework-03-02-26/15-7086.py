def DEL(n, m):
    return n % m == 0

def f(x):
    B = x in range(50, 71)
    return DEL(x, A) or (B <= (not DEL(x, 16)))

for A in range(1, 1000)[::-1]:
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break
        