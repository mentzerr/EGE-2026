def f(a, b, m):
    if a + b <= 108: return m % 2 == 0
    if m == 0: return 0
    h = [f(a - 2, b, m - 1),
        f(a, b - 2, m - 1),
        f((a + 1) // 2, b, m - 1),
        f(a, (b + 1) // 2, m - 1)]
    return any(h) if m % 2 == 1 else all(h)

print('19)', [b for b in range(49, 1000) if f(60, b, 2)])
print('20)', [b for b in range(49, 1000) if f(60, b, 3) and not f(60, b, 1)])
print('21)', [b for b in range(49, 1000) if f(60, b, 4) and not f(60, b, 2)])
