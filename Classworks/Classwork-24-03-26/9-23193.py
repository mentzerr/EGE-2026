with open('9_23193.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, line in enumerate(data, start = 1):
    line_pov = [x for x in line if line.count(x) == 3]
    line_ne_pov = set([x for x in line if x not in line_pov])
    if len(line_pov) == 3 and len(line_ne_pov) == 3:
        if line_pov[0] > sum(line_ne_pov) / len(line_ne_pov):
            print(pos)
