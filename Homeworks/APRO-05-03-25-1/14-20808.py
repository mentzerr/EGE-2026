def conv(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for x in range(1, 2031):
    a = 7**170 + 7**100 - x
    s = conv(a, 7)
    if s.count('0') == 73:
        print(x)
