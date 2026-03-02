a = [int(x) for x in open('17_25356.txt')]

max_el = max([int(x) for x in a if abs(x) % 100 == 30])

ans = []
for x, y, z in zip(a, a[1:], a[2:]):
    if (len(str(abs(x))) == 4) + (len(str(abs(y))) == 4) + (len(str(abs(z))) == 4) == 0 and \
        x + y + z > max_el:
        ans.append(x + y + z)
print(len(ans), max(ans))
