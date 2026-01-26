
for x in range(1, 2006):
    a = 4**163 * 5 + 12**62 - x
    res = ''
    while a:
        res += str(a % 5)
        a //= 5
    if res.count('1') < res.count('4'):
        print(x)

