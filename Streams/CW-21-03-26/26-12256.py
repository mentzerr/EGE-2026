with open('26_12256.txt') as file:
    S, N = map(int, file.readline().split())
    boxes = sorted([int(x) for x in file])

volume = []

for box in boxes:
    if sum(volume) + box <= S:
        volume.append(box)
free_space = S - sum(volume[:-1])
print(len(volume), max(x for x in boxes if x <= free_space))