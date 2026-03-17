with open('17_4622.txt') as file:
    data = [int(x) for x in file]

min_el = min([n for n in data if n > 0 and n % 19 == 0])

ans = []
for x, y in zip(data, data[1:]):
    if (x + y) < min_el:
        ans.append(x + y)
print(len(ans), abs(max(ans)))
