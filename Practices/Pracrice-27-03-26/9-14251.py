with open('9_14251.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = []
for line in data:
    line_pov = [x for x in line if line.count(x) == 2]
    line_ne_pov = set([x for x in line if x not in line_pov])
    if len(line_pov) == 4 and len(line_ne_pov) == 3:
        if sum(line_pov) <= sum(x for x in line if x % 2 == 1):
            print(sum(line))
            break