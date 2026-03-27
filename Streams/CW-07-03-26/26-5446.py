with open('26_5446.txt') as file:
    N = int(file.readline())
    tubes = sorted([tuple(map(int, i.split())) for i in file], key = lambda x: (-x[0] + x[1], -x[0]))

last_picked_tube = tubes[0]
k = 1

for tube in tubes:
    if last_picked_tube[0] - 2 * last_picked_tube[1] - tube[0] >= 3:
        last_picked_tube = tube
        k += 1

print(k, last_picked_tube[0])
