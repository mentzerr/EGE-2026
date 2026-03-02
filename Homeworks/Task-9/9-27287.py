f = open('1')

ans = []
for pos, s in enumerate(f, start = 1):
    a = [int(x) for x in s.split()]
    a3 = [int(x) for x in a if a.count(x) == 3]
    a1 = [int(x) for x in a if a.count(x) == 1]
    if len(a3) == 6 and len(a1) == 1:
        if a1[0] < min(a3):
            ans.append([pos, max(a3)])

ans = sorted(ans, key = lambda x:(x[0], -x[1]))
print(ans[0][1])