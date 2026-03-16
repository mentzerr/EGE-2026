with open('17_12249.txt') as file:
    data = [int(x) for x in file]

max_el = max(x for x in data if len(str(abs(x))) == 5 and abs(x) % 10 == 3)

ans = []
for x, y, z in zip(data, data[1:], data[2:]):
    if (abs(x) % 10 == 3) + (abs(y) % 10 == 3) + (abs(z) % 10 == 3) >= 1 and \
            (x + y + z) <= max_el:
                ans.append(x + y + z)
print(len(ans), max(ans))
