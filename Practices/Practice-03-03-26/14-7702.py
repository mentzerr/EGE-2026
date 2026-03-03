from string import printable as alph

ans = set()
for y in range(9, 18):
    for x in range(0, y):
        num1 = int(f'5{alph[x]}{alph[y]}A', 18)
        num2 = int(f'18{alph[x]}7', y)
        ans |= {num1 + num2}
print(len(ans))
