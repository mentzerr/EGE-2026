a = [int(x) for x in open('17_27301.txt')]

max_el = max([x for x in a if str(abs(x))[:2] == '45'])

ans = []
for x, y, z in zip(a, a[1:], a[2:]):
    if ((x < 0) + (y < 0) + (z < 0) == 1) and x + y + z >= max_el:
        if abs(x + y + z) % 100 == 45:
            ans.append(x + y + z)
print(len(ans), min(ans))


