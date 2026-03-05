ans = []
for x in range(1, 2031):
    k0 = 0
    a = 6**2030 + 6**100 - x
    while a:
        if a % 6 == 0: k0 += 1
        a //= 6
    ans.append(k0)
print(min(ans))