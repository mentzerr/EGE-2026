def f(a, b, m):
    if a + b >= 77: return m % 2 == 0
    if m == 0: return False
    h = [f(a + 3, b, m - 1),
         f(a * 3, b, m - 1),
         f(a, b + 3, m - 1),
         f(a, b * 3, m - 1)]
    return any(h) if m % 2 == 1 else all(h)

print('19)', [s for s in range(1, 65) if f(12, s, 2)][0])
print('20)', [s for s in range(1, 65) if f(12, s, 3) and not f(12, s, 1)][:2])
print('21)', len([s for s in range(1, 65) if f(12, s, 4) and not f(12, s, 2)]))
