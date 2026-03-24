with open('9_9740.txt') as file:
    data = [list(map(int, i.split())) for i in file]

k = 0
for line in data:
    line_pov = [x for x in line if line.count(x) == 3]
    line_ne_pov = [x for x in line if x not in line_pov]
    if len(line_pov) == 3 and len(set(line_ne_pov)) == 4:
        if sum(line_ne_pov) / len(line_ne_pov) <= line_pov[0]:
            k += 1
print(k)