def F(start, end, k = 0):
    if start % 2 == 0: k += 1
    if start == end and k <= 15: return 1
    if start > end or k > 15: return 0
    return F(start + 2, end, k) + F(start + 3, end, k) + F(start * 2 + 1, end, k)

print(F(1, 55))
