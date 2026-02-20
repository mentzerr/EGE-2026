def F(start, end):
    if start == end: return 1
    if start < end or start == 8: return 0
    return F(start - 1, end) + F(start - 4, end) + F(start // 3, end)

print(F(19, 14) * F(14, 2))