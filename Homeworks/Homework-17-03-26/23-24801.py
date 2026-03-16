def f(start, end, number):
    if start == end: return 1
    if start > end or start == number: return 0
    return f(start + 1, end, number) + f(start + 2, end, number) + \
        f(start + 4, end, number) + f(start + 8, end, number)

ans0 = f(16, 24, 32)*f(24, 48, 32)
ans1 = f(16, 32, 24)*f(32, 48, 24)
print(ans0 + ans1)