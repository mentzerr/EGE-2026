with open('17_9748.txt') as file:
    data = [int(x) for x in file]

max_el = max([x for x in data if x % 100 == 15])

ans = []
for x, y, z in zip(data, data[1:], data[2:]):
    if (len(str(x)) == 4) + (len(str(y)) == 4) + (len(str(z)) == 4) == 1 \
        and (x + y + z) >= max_el:
        ans.append(x + y + z)
print(len(ans), max(ans))
