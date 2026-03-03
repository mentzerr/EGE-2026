file = open('10')

k = 0
for pos, s in enumerate(file, start = 1):
    a = sorted([int(x) for x in s.split()])
    if (a[0] + a[-1]) ** 2 > a[1]**3 + a[2] ** 3 and a[0]+a[3]!=a[1]+a[2]:
        k += pos
print(k)

