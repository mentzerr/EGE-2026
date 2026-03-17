with open('17_17558.txt') as file:
    data = [int(x) for x in file]

k_32 = len([x for x in data if x % 32 == 0])

ans = []
for x, y in zip(data, data[1:]):
    if (x < 0) + (y < 0) >= 1 and (x + y) < k_32:
        ans.append(x + y)
print(len(ans), max(ans))