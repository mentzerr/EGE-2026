def f(start, end):
    if start == end: return 1
    if start < end: return 0
    return f(start - 3, end) + f(start - 5, end) + f(start // 3, end)

ans_1 = f(80, 18)*f(18, 3)
ans_2 = f(80, 38)*f(38, 3)
ans_3 = f(80, 38)*f(38, 18)*f(18, 3)
print(ans_1 + ans_2 - ans_3)
