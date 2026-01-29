ans = []
for N in range(1, 1000):
    b = f'{N:b}'
    if b.count('1') % 2 == 0:
        b = '10' + b[:-2] + '00'
    else:
        b = '11' + b[:-2] + '11'
    R = int(b, 2)
    if N < 30:
        ans.append(R)
print(max(ans))