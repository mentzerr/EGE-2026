def conv(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'
ans = []
for N in range(0, 1000):
    h = conv(N, 4)
    if int(h) % 2 == 0:
        h = '12' + h + conv(int(h[-1] * 3), 4)
    else:
        h = '13' + h + '21'
    R = int(h, 4)
    if R > 50:
        ans.append(R)
print(min(ans))