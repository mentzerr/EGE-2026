with open('9_7030.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    line_pov = sorted(set([x for x in line if line.count(x) == 2]))
    if len(line_pov) == 3:
        if line_pov[-1] ** 2 == line_pov[0] ** 2 + line_pov[1] ** 2:
            cnt += 1
print(cnt)
