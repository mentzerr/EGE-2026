def check(num):
    return len(str(abs(num))) == 4

with open('17_9786.txt') as file:
    data = [int(x) for x in file]

max_el = max(x for x in data if abs(x) % 100 == 25)

ans = []
for x, y, z in zip(data, data[1:], data[2:]):
    if sum((check(num) for num in [x, y, z])) <= 2 and (x + y + z) <= max_el:
        ans.append(x + y + z)
print(len(ans), max(ans))