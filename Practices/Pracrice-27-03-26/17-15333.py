with open('17_15333.txt') as file:
    data = [int(x) for x in file]

max_el = max(x for x in data if x % 19 == 0)

ans = []
for nums in zip(data, data[1:]):
    if sum(num > max_el for num in nums) >= 1:
        ans.append(sum(nums))
print(len(ans), max(ans))