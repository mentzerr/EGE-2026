with open('17_2997.txt') as file:
    data = [int(x) for x in file]

nums_3 = [int(str(abs(i))[1]) for i in data if len(str(abs(i))) == 3]
moda = max(set(nums_3), key = lambda x: nums_3.count(x))

ans = []
for x, y in zip(data, data[1:]):
    if (str(x)[-1] == str(moda)) + (str(y)[-1] == str(moda)) >= 1:
        ans.append(x + y)
print(len(ans), max(ans))


