with open('17_6791.txt') as file:
    data = [int(x) for x in file]

min_el_sqrt = min(x for x in data if str(x)[-2:] == '68') ** 2

ans = []
for nums in zip(data, data[1:]):
    if sum(str(num)[-2:] == '68' for num in nums) == 1:
        if nums[0] ** 2 + nums[1] ** 2 >= min_el_sqrt:
            ans.append(nums[0] ** 2 + nums[1] ** 2)
print(len(ans), max(ans))