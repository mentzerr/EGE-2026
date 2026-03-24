with open('9_9832.txt') as file:
    data = [list(map(int, i.split())) for i in file]


for line in data:
    data_p = [x for x in line if line.count(x) == 2]
    data_ost = [x for x in line if x not in data_p]
    if len(data_p) == 4 and len(data_ost) == 3 and max(line) not in data_p:
        print(sum(line))
        break
######################################################################################

with open('9_9832.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for line in data:
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1, 1, 1, 2, 2]:
        if line.count(max(line)) == 1:
            print(sum(line))
            break
