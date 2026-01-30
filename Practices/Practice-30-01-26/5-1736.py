ans = []
for N in range(1, 10000):
    b = f'{N:b}'
    b = b.replace('0', '00')
    b = b.replace('1', '11')
    R = int(b, 2)
    if R > 63:
        ans.append(R)
print(min(ans))
