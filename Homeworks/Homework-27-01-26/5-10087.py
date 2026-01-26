ans = []
for N in range(1, 1000):
    b = f'{N:b}'
    if N % 3 == 0:
        b = b + b[-3:]
    else:
        o = f'{3*(N%3):b}'
        b = b + o
    R = int(b, 2)
    if R > 151:
        ans.append(R)
print(min(ans))