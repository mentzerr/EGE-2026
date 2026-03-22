with open('17_3749.txt') as file:
    data = [int(x) for x in file]

max_el = max(x for x in data if x ** 0.5 == int(x ** 0.5)) * 3

ans = []
for nums in zip(data, data[1:]):
    if (nums[0]*nums[1]) ** .5 == int((nums[0]*nums[1]) ** .5) and \
        sum(num <= max_el for num in nums) >= 1:
            ans.append((nums[0]*nums[1]) ** 0.5)
print(len(ans), min(ans) + max(ans))