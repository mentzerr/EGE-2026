def f(n):
    for x in range(1, 1000):
        for y in range(1, 1000):
            z = (9*x + y > A) or (x >= 36) or (y >= 18)
            if not z:
                return False
    return True

for A in range(1000, 0, -1):
    if f(A):
        print(A)
        break

