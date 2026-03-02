def conv(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 10000):
    t = conv(N, 3)
    if N % 3 == 0:
        t = t + t[-2:]
    else:
        s = conv(sum(map(int, str(t))) * 3, 3)
        t = t + s
    R = int(t, 3)
    if R > 208 and R % 2 == 1:
        ans.append(R)
print(min(ans))

