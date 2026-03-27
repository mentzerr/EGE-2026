ans = []
for N in range(1, 1000000):
    b = f'{N:b}'
    if N % 5 == 0:
        b = b + f'{5:b}'
    else:
        b = b + '1'

    if int(b, 2) % 7 == 0:
        b = b + f'{7:b}'
    else:
        b = b + '1'
    R = int(b, 2)
    if R < 1855663:
        ans.append(N)
print(max(ans))