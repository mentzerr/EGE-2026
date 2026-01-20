def CIF(x, y):
    return str(x)[-1] == str(y)[-1]

def f(x):
    return (not CIF(x, 5) and CIF(x, 4)) <= (x > A - 11)

for A in range(1, 1000)[::-1]:
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break