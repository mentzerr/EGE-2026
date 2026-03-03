def conv(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 10000):
    t = conv(N, 3)
    if N % 5 == 0:
        t = t + t[-2:]
    else:
        t = t + conv((N % 5)*7, 3)
    R = int(t, 3)
    if R <= 273:
        ans.append(N)
print(max(ans))

