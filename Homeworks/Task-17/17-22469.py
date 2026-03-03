a = [int(x) for x in open('17_22469.txt')]

sum_el = sum([x for x in a if x % 2 == 1 and len(str(abs(x))) == 5])

ans = []
for x, y in zip(a, a[1:]):
    if (str(x)[-1] == str(sum_el)[-1]) + (str(y)[-1] == str(sum_el)[-1]) == 1:
        ans.append(x*y)
print(len(ans), max(ans))
