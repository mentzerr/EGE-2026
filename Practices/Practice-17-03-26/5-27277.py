def conv(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 10000):
    T = conv(N, 3)
    if N % 3 != 0:
        T = '1' + T + T[-3:]
    else:
        T = T + conv(sum(map(int, str(T))) * 8, 3)
    R = int(T, 3)
    ans.append([abs(1220 - R), R])
print(min(ans))