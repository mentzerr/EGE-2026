def f(x, y):
    B = x in range(50, 71)
    return (2*x + y != 150) or (not B) or A > y

for A in range(1, 1000):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(A)
        break
