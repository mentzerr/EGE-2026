def f(s, m):
    if s >= 444: return m % 2 == 0
    if m == 0: return False
    h = [f(s + 2, m - 1),
         f(s + 5, m - 1),
         f(s * 3, m - 1)]
    return any(h) if m % 2 == 1 else all(h)

print('19)', min([s for s in range(1, 401) if f(s, 2)]))
print('20)', [s for s in range(1, 401) if f(s, 3) and not f(s, 1)][:2])
print('21)', max([s for s in range(1, 401) if f(s, 4) and not f(s, 2)]))