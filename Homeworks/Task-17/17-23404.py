a = [int(x) for x in open('17_23404.txt')]

min_el = abs(min([int(x) for x in a if abs(x) % 1000 == 152]))


ans = []
for x, y in zip(a, a[1:]):
    if x + y < min_el:
        ans.append(abs(x) + abs(y))

print(len(ans), max(ans))
