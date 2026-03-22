def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0: return False
    return True

with open('17_9993.txt') as file:
    data = [int(x) for x in file]

max_el = max(x for x in data if str(x)[-2:] == '17')

ans = []
for nums in zip(data, data[1:]):
    if sum(is_prime(num) for num in nums) == 1:
        if sum(nums) % max_el == 0:
            ans.append(nums[0]*nums[1])
print(len(ans), max(ans))
