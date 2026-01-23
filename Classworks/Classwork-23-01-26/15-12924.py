def f(x):
    P = x in range(2, 21, 2)
    Q = x in range(3, 31, 3)
    A = 1
    return (A <= P) and ((not Q) <= (not A))

As = []
for x in range(2, 31):
    if f(x):
        As.append(x)
print(As)