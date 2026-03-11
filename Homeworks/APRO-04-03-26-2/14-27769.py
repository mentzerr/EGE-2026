from string import printable as p

ans = []
for x in range(0, 22):
    num1 = int(f'12313{p[x]}57', 22)
    num2 = int(f'1{p[x]}34561', 22)
    num = num1 + num2
    if num % 21 == 0:
        ans.append([x, num // 21])
print(max(ans))