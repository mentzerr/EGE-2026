with open('9_17522.txt') as file:
    data = [list(map(int, i.split())) for i in file]

k = 0
for line in data:
    if max(line) < sum(line) - max(line):
        if len(set(line)) == 3:
            k += 1
print(k)