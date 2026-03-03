from math import prod
file = open('7')

k = 0
for s in file:
    a = [int(x) for x in s.split()]

    s = sorted(a)
    if (a.count(s[-1]) == 1) + \
            (a[0] != s[0] and a[-1] != s[-1] and a[0] != s[-1] and a[-1] != s[0]) + \
            (prod(s[-3:]) % s[0] == 0) == 1:
            k += 1
print(k)