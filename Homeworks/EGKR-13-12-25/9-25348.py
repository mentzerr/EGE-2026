file = open('9-EGKR')

k = 0
for s in file:
    a = [int(x) for x in s.split()]
    a3 = [int(x) for x in a if a.count(x) == 3]
    ar = [int(x) for x in a if a.count(x) == 1]
    if len(a3) == 3 and len(ar) == 4:
        if max(a) not in a3:
            k += 1
print(k)
