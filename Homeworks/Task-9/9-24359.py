file = open('6')

ans = []
for pos, s in enumerate(file, start = 1):
    a = [int(x) for x in s.split()]
    rz_a = [x for x in a if a.count(x) == 1]
    a3 = [x for x in a if a.count(x) == 3]
    a2 = [x for x in a if a.count(x) == 2]
    if len(a3) == 3 and len(a2) == 2 and len(rz_a) == 3 and sum(a3 + a2) > sum(rz_a):
        ans.append([pos, sum(a)])
print(max(ans)[1])
