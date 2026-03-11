ans = []
for N in range(1, 1000):
    b = f'{N:b}'
    if N % 3 == 0:
        b = b + b[-3:]
    else:
        b = b + f'{(N % 3)*3:b}'
    R = int(b, 2)
    if 120 < R < 140:
        ans.append([abs(130 - R), N])
ans = sorted(ans, key = lambda x: (x[0], -x[1]))
print(ans[0][1])