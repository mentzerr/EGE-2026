def check(num):
    if len(str(abs(num))) == 5:
        return 1
    return 0

a = [int(x) for x in open('17_23376.txt')]

max_el = max([int(x) for x in a if check(x) and x % 100 == 37])

ans = []
for x, y in zip(a, a[1:]):
    if check(x) + check(y) == 1 and (x + y) ** 2 > max_el ** 2:
        ans.append(x + y)
print(len(ans), max(ans))
