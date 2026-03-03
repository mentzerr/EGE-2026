a = [int(x) for x in open('17_23952.txt')]

max_el = max([x for x in a if x % 100 == 93])

ans = []
ans2 = []
for x, y in zip(a, a[1:]):
    if (x > max_el) + (y > max_el) == 1 and (str(x)[0] == '9' or str(y)[0] == '9'):
        ans += [x if x > max_el else y]

print(len(ans), sum(ans))
