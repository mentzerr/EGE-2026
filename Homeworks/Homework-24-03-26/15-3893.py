def DEL(n, m):
    return n % m == 0

def f(x):
    return DEL(A, 25) and ((DEL(x, 24) and DEL(x, 75)) <= DEL(x, A))

k = 0
for A in range(-24*75*10, 24*75*10+1):
    if A == 0: continue
    if all(f(x) for x in range(-10000, 10000)):
        k += 1
print(k)