ans = []
for p in range(11, 37):
    for x in range(1, 500_001):
        num1 = int('29A1', p)
        num2 = int('47771', p)
        num3 = int('12A', p)
        num4 = int('1_000_000', 10)
        num5 = x
        if num1 + num2 + num3 == num4 + num5:
            ans.append(p)
print(max(ans))
