a = 3*17**777 + 15*17**250 - 6*17**100 + 2

ans = []
while a:
    ans.append(a % 17)
    a //= 17

k = 0
for i in set(ans):
    if i % 2 == 0:
        k += 1
print(k)


