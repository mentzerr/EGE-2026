def F(start, end, l):
    if start == end and len(l) >= 52: return 1
    if start > end: return 0
    return F(start + 2, end, l | {start + 2}) + F(start * 3, end, l | {start + 3}) + F(start * 4, end, l | {start * 4})

print(F(2, 400, set()))