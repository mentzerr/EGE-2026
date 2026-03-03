a = [int(x) for x in open('17_24074.txt')]

min_el = min([x for x in a if len(str(x)) == 3 and x % 10 == 9])

ans = []
for x, y in zip(a, a[1:]):
    if (len(str(x)) == 2) + (len(str(y)) == 2) >= 1:
        if (x + y) % min_el == 0:
            ans.append(x + y)
print(len(ans), max(ans))

