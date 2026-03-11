a = [int(x) for x in open('17_27629.txt')]

max_el = max([x**2 for x in a if abs(x) % 100 == 43 and len(str(abs(x))) == 4])

ans = []
for x, y in zip(a, a[1:]):
    if (len(str(abs(x))) == 4) + (len(str(abs(y))) == 4) >= 1 and \
            (x + y) ** 2 < max_el:
        ans.append((x + y)**2)
print(len(ans), max(ans))
