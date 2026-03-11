with open('26_27779.txt') as file:
    N = int(file.readline())
    cakes = sorted([int(x) for x in file], reverse=True)

last_picked_cake = cakes[0]

k = 1
for cake in cakes:
    if last_picked_cake - cake >= 8:
        last_picked_cake = cake
        k += 1
print(k, last_picked_cake)
