for x in range(1, 1000):
    k = 0
    a = 7**666 + 7**333 + 49**x - 343
    while a:
        if a % 7 == 6: k += 1
        a //= 7
    if k == 49:
        print(x)
        break
        