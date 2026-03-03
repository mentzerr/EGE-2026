def check1(num):
    return str(num)[0] == str(num)[-1]

def check2(num):
    return len(str(num)) == 5 and str(num)[1] == '7'

a = [int(x) for x in open('17_23949.txt')]

ans = []
for x, y, z in zip(a, a[1:], a[2:]):
    if check1(x) + check1(y) + check1(z) == 1 and \
        check2(x) + check2(y) + check2(z) == 2:
        ans.append(max(x, y, z))
print(len(ans), sum(ans))

