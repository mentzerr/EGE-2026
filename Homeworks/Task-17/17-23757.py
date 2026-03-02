a = [int(x) for x in open('17_23757.txt')]

min_el = min([int(x) for x in a if 10 <= x < 100])

ans = []
for x, y in zip(a, a[1:]):
    if (len(str(x)) == 2) + (len(str(y)) == 2) == 1 and (x + y) % min_el == 0:
        ans.append(x + y)
print(len(ans), max(ans))
