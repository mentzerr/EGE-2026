with open('17_2473.txt') as file:
    data = [int(x) for x in file]

ans = []
for x, y in zip(data, data[1:]):
    if (x % 7 == 0) + (y % 7 == 0) >= 1:
        if (abs(x) % 10 == 3) + (abs(y) % 10 == 3):
            ans.append(x + y)
print(len(ans), min(ans))
