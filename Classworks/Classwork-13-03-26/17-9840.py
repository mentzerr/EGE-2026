with open('17_9840.txt') as file:
    data = [int(x) for x in file]

max_el_sqrt = max(x for x in data if abs(x) % 100 == 39 and len(str(abs(x))) == 4) ** 2

ans = []
for x, y in zip(data, data[1:]):
    if (len(str(abs(x))) == 4) + (len(str(abs(y))) == 4) == 1 and \
            (x + y) ** 2 <= max_el_sqrt:
        ans.append(x + y)
print(len(ans), max(ans))
