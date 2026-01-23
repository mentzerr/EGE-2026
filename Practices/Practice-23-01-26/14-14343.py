def conv(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

x = 5*343**2031 + 4*49**2142 - 3*7**111 + 7**222
c = conv(x, 7)
print(sum(map(int, c)))

