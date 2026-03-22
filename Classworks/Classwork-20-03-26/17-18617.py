with open('17_18617.txt') as file:
    data = [int(x) for x in file]

ans = []
for nums in zip(data, data[1:]):
    if sum(num % 3 == max(data) % 3 for num in nums) >= 1:
        if sum(num % 7 == min(data) % 7 for num in nums) >= 1:
            ans.append(sum(nums))
print(len(ans), max(ans))
