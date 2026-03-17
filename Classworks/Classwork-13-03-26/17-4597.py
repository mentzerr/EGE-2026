with open('17_4597.txt') as file:
    data = [int(x) for x in file]

min_el = min(data)

ans = []
for x, y in zip(data, data[1:]):
    if any([(x % 117 == min_el), (y % 117 == min_el)]):
        ans.append(x + y)
print(len(ans), max(ans))
