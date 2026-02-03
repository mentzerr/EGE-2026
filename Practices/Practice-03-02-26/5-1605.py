ans = []
for N in range(1, 10000):
    b = f'{N+2:b}'
    b = b + str(sum(map(int, b)) % 2)
    b = b + str(sum(map(int, b)) % 2)
    R = int(b, 2)
    if R < 61:
        ans.append(N)
print(max(ans))