def check(num):
    return len(str(abs(num))) == 4

a = [int(x) for x in open('17_23276.txt')]

max_el = max([x for x in a if abs(x) % 100 == 25])

ans = []
for x, y, z in zip(a, a[1:], a[2:]):
    if check(x) + check(y) + check(z) <= 2 and x + y + z <= max_el:
        ans.append(x + y + z)
print(len(ans), max(ans))

