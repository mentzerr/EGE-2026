def f(x, y):
    return (78125 != y + 4 * x) or (A > x) and (A > y)

pair = []
for x in range(1, 1000000):
    y = 78125 - 4*x
    if y > 0:
        pair.append([x, y])

for A in range(1, 100000):
    if all(f(x, y) for x, y in pair):
        print(A)
        break