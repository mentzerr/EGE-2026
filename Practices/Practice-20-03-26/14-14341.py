from string import printable as p

ans = []
for x in range(0, 22):
    num1 = int(f'56{p[x]}C20', 22)
    num2 = int(f'89F{p[x]}2', 22)
    num3 = int(f'H24{p[x]}K21', 22)
    num = num1 + num2 + num3
    if num % 21 == 0:
        ans.append([x, num // 21])
print(min(ans))