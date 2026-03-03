file = open('9')

ans = []
for pos, s in enumerate(file, start = 1):
    l = sorted([int(x) for x in s.split()])
    
    if l[-2] ** 2 > l[0] * l[-1] and sum(l) % 2 == 0:
        l9 = [x for x in l if x < 90]
        if sum(l9) % 10 == 4:
            ans.append([pos, sum(l)])
print(min(ans))
