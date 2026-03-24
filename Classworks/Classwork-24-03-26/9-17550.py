with open('9_17550.txt') as file:
    data = [list(map(int, i.split())) for i in file]

k = 0
for line in data:
    line_pov = [x for x in line if line.count(x) == 3]
    line_ne_pov = set([x for x in line if x not in line_pov])
    if len(line_pov) == 3 and len(line_ne_pov) == 3:
        if sum(line_pov) ** 2 > sum(line_ne_pov) ** 2:
            k += 1
print(k)
