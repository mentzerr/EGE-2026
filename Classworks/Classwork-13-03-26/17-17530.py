with open('17_17530.txt') as file:
    data = [int(x) for x in file]

ans = []
for x, y in zip(data, data[1:]):
    if (x % 55 == min(data)) + (y % 55 == min(data)) >= 1:
        ans.append(x + y)
print(len(ans), min(ans))