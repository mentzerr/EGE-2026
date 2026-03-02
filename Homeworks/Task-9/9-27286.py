ans = []
for pos, s in enumerate(open('2'), start = 1):
    a = [int(x) for x in s.split()]
    a3 = [int(x) for x in a if a.count(x) == 3]
    a2 = [int(x) for x in a if a.count(x) == 2]
    a1 = [int(x) for x in a if a.count(x) == 1]
    if len(a3) == 3 and len(a2) == 2 and len(a1) == 1:
        ap = [x for x in a2 for x in a3]
        if a1[0] < min(ap):
            ans.append([pos, abs(min(ap))])

ans = sorted(ans, key = lambda x: (-x[0], x[1]))
print(ans[0][1])