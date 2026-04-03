with open('17_21595.txt') as file:
    data = [int(x) for x in file]

amount = len([x for x in data if len(str(abs(x))) == 4 and abs(x) % 10 == 3]) ** 2

ans = []
for nums in zip(data, data[1:], data[2:]):
    if sum(sorted(nums)[-2:]) > amount:
        ans.append(sum(nums))
print(len(ans), abs(max(ans)))

