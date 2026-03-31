with open('17.txt') as file:
    data = [int(x) for x in file]

max_el = max(x for x in data if len(str(x)) == 2)

ans = []
for nums in zip(data, data[1:]):
    if sum(len(str(x)) == 2 for x in nums) == 1:
        if sum(nums) % max_el == 0:
            ans.append(sum(nums))
print(len(ans), max(ans))

