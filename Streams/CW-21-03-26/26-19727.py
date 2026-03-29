with open('26.2_19727.txt') as file:
    M, N = map(int, file.readline().split())
    cans = sorted([int(x) for x in file])


volume_train = []

for can in cans:
    if sum(volume_train) + can <= M:
        volume_train.append(can)

free_space = M - sum(volume_train[:-1])


print(len(volume_train), len([x for x in cans if x > free_space]))