
for x in range(1, 27_001):
    a = 3 * 27 ** 9 + 2 * 27 ** 6 + 27 ** 3 - x
    k0 = 0
    while a:
        if a % 27 == 0: k0 += 1
        a //= 27
    if k0 == 6:
        print(x)
        break
