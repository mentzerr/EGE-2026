def conv(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

for N in range(1, 1000):
    v = conv(N, 8)
    if v[0] == '5':
        v = v.replace('2', '*')
        v = v.replace('1', '2')
        v = v.replace('*', '2')
        v = '11' + v
    else:
        v = '2' + v[1:] + '10'
    R = int(v, 8)
    if R < 1354:
        print(N)
