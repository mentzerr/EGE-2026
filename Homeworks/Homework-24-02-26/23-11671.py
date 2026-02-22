def f(start, k):
    if k == 15: return {start}
    return f(start + 10, k + 1) | f(start - 5, k + 1)

print(len(f(1, 0)))