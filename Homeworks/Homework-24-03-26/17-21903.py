with open('17_21903.txt') as file:
    data = [int(x) for x in file]

min_el = min(x for x in data if str(x)[-2:] == '15' and len(str(abs(x))) == 3) ** 2

ans = []
for nums in zip(data, data[1:], data[2:]):
    if all([num > 0 for num in nums]) or all([num < 0 for num in nums]):
        if min(nums) * max(nums) > min_el:
            ans.append(min(nums) * max(nums))
print(len(ans), min(ans))

