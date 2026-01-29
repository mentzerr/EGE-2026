from string import printable as alph
ans = []
for x in range(10, 14):
    for y in range(9, x):
        num1 = int(f'7{alph[x]}37{alph[y]}', 14)
        num2 = int(f'9{alph[y]}63', x)
        num3 = int('15148', y)
        num = num1 + num2 - num3
        ans.append([num, num // (x + y)])
print(max(ans)[1])