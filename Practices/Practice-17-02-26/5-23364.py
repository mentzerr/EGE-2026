def conv(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'

ans = []
for N in range(1, 100000):
    t = conv(N, 3)
    if N % 3 == 0:
        t = '1' + t + '02'
    else:
        t = t + conv((N % 3) * 4, 3)

    R = int(t, 3)
    if R < 100:
        ans.append(N)
print(max(ans))
