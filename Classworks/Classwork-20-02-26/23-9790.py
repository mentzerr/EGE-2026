def F(start, end):
    if start == end: return 1
    if start < end or start in (9, 16): return 0
    return F(start - 1, end) + F(start - 2, end) + F(start // 3, end)

print(F(19, 3))