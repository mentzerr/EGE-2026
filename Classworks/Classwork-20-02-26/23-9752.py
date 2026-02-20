def F(start, end):
    if start == end: return 1
    if start > end or start == 17: return 0
    return F(start + 2, end) + F(start + 3, end) + F(start * 2, end)

print(F(3, 10) * F(10, 25))