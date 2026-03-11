ans = []
for N in range(1, 10000):
    b = f'{N:b}'
    if N % 2 == 0:
        b = '10' + b
    else:
        b = '1' + b + '01'
    R = int(b, 2)
    if N > 18:
        ans.append(R)
print(min(ans))
