with open('9_111.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, line in enumerate(data, start = 1):
    line_pov = [x for x in line if line.count(x) == 2]
    line_ne_pov = set([x for x in line if line.count(x) == 1])
    if len(line_pov) == 2 and len(line_ne_pov) == 4:
        if line_pov[0] >= sum(line_ne_pov) / len(line_ne_pov):
            print(pos, line)
            break