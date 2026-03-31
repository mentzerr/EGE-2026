def conv(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 10000):
    H = conv(N, 4)
    if N % 4 == 0:
        H = H + H[:2]
    else:
        H = H + conv((N % 4) * 4, 4)
    R = int(H, 4)
    if R > 291:
        ans.append(R)
print(min(ans))