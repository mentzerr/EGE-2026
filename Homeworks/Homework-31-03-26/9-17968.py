with open('9_17968.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    line.sort(reverse=True)
    if line[0] < sum(line[1:]) and \
    sum(x for x in line if x % 2 == 0) == sum(x for x in line if x % 2 != 0):
        cnt += 1
print(cnt)