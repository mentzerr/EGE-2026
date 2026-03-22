def check1(num):
    return str(num)[0] == str(num)[-1]

def check2(num):
    return len(str(num)) == 4 and str(num)[1] == '2'

with open('17_23902.txt') as file:
    data = [int(x) for x in file]

sum_el = 0
ans = []
for nums in zip(data, data[1:], data[2:]):
    if sum(check1(num) for num in nums) == 1:
        if sum(check2(num) for num in nums) == 2:
            ans.append(max(nums))


print(len(ans), sum(ans))