def conv(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'

ans = []
for N in range(1, 1000):
    t = conv(N, 3)
    if N % 3 == 0:
        t = t + t[-2:]
    else:
        s = sum(map(int, str(t)))
        s3 = conv(s, 3)
        t = t + s3
    R = int(t, 3)
    if R > 220 and R % 2 == 0:
        ans.append(R)
print(min(ans))