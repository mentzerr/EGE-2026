def f(a, b, m):
    if a + b <= 100: return m % 2 == 0
    if m == 0: return False
    h = [f(a - 3, b - 3, m - 1),
         f(a // 2, b, m - 1),
         f(a, b // 2, m - 1)]
    return any(h) if m % 2 == 1 else all(h)

print('19)', [b for b in range(53, 1000) if f(48, b, 2)])
print('20)', [b for b in range(53, 1000) if f(48, b, 3) and not f(48, b, 1)])
print('21)', [b for b in range(53, 1000) if f(48, b, 4) and not f(48, b, 2)])