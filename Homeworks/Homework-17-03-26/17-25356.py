with open('17_25356.txt') as file:
    data = [int(x) for x in file]

max_el = max(i for i in data if abs(i) % 100 == 30)

ans = []
for x, y, z in zip(data, data[1:], data[2:]):
    if (len(str(abs(x))) == 4) + (len(str(abs(y))) == 4) + (len(str(abs(z))) == 4) == 0 and \
            (x + y + z) > max_el:
        ans.append(x + y + z)
print(len(ans), max(ans))