for X in range(1, 50)[::-1]:
    for Y in range(1, 50)[::-1]:
        cnt_0 = 0
        ex = 5**50 + 5**30 - 5 ** X - Y - 5 ** Y - X
        while ex:
            if ex % 5 == 0: cnt_0 += 1
            ex //= 5
        if cnt_0 == 10:
            print(X * Y)
        break