with open('26_17786.txt') as file:
    N, S = map(int, file.readline().split())
    BERRIES = sorted([int(x) for x in file if 7000 <= int(x) <= 12000], reverse = True)
    S = S * 1000

volume_truck = []

for BERRY in BERRIES:
    if sum(volume_truck) + BERRY <= S:
        volume_truck.append(BERRY)

free_space = S - sum(volume_truck[:-1])
print(len(volume_truck), max(x for x in BERRIES if x <= free_space))

