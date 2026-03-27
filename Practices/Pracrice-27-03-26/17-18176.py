with open('17_18176.txt') as file:
    data = [int(x) for x in file]

min_el = min(x for x in data if x > 0 and str(x)[-1] == '4')

ans = []
for nums in zip(data, data[1:], data[2:]):
    if sum([sum(map(int, str(abs(num)))) for num in nums]) == min_el:
        ans.append(sum(nums))
print(len(ans), max(ans))
