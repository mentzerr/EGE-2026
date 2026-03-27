from math import prod

with open('17_11236.txt') as file:
    data = [int(x) for x in file]

min_el_sqrt = min(x for x in data if len(str(abs(x))) == 2) ** 2
max_el_4 = max(x for x in data if len(str(abs(x))) == 4 and x % 10 == 1)

ans = []
for nums in zip(data, data[1:], data[2:]):
    if sum(num > min_el_sqrt for num in nums) == 2:
        if prod(abs(num) for num in nums) % max_el_4 == 0:
            ans.append(sum([abs(x) for x in nums]))
print(len(ans), max(ans))

