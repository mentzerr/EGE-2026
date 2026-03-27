def conv(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 10000):
    P = conv(N, 5)
    if sum(map(int, P)) % 5 == 0:
        P = P.replace('0', '*')
        P = P.replace('1', '0')
        P = P.replace('*', '1')
        P = P + '14'
    else:
        P = P + '33'
        P = '44' + P[2:]
    R = int(P, 5)
    if R > 370:
        ans.append([R, N])

print(min(ans))
