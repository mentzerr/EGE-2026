with open('9_17628.txt') as file:
    data = [list(map(int, i.split())) for i in file]

k = 0
for line in data:
    line = sorted(line)
    if line[0] + line[-1] <= sum(line[1:-1]):
        k += 1
print(k)

