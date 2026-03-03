file = open('8')

for pos, s in enumerate(file, start = 1):
    a = [int(x) for x in s.split()]
    ap = [x for x in a if a.count(x) in range(2, 9)]
    an = [x for x in a if a.count(x) == 1]
    if sum(ap) ** 2 > sum(an) ** 2 and sum(a) % 2 != 0:
        print(pos)