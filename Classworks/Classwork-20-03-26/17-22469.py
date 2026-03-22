with open('17_22469.txt') as file:
    data = [int(x) for x in file]

sum_5 = sum(x for x in data if abs(x) % 2 == 1 and len(str(abs(x))) == 5)

ans = []
for nums in zip(data, data[1:]):
    if sum(str(num)[-1] == str(sum_5)[-1] for num in nums) == 1:
        ans.append(nums[0]*nums[1])
print(len(ans), max(ans))
