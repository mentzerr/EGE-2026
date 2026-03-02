a = [int(x) for x in open('17_23563.txt')]

min_el = min([int(x) for x in a if x > 0 and x % 35 == 0])

ans = []
for x, y in zip(a, a[1:]):
    if x != y and abs(x - y) % min_el == 0:
        ans.append(x + y)
print(len(ans), max(ans))
