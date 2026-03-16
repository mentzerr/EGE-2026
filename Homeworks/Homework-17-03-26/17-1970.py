with open('17_1970.txt') as file:
    data = [int(x) for x in file]

ans = []
for x, y in zip(data, data[1:]):
    if (abs(x) % 3 == 0) + (abs(y) % 3 == 0) >= 1:
        ans.append(x + y)
print(len(ans), max(ans))