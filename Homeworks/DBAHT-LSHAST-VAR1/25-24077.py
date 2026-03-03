from fnmatch import fnmatch

for N in range(4317014 - 4317014 % 2026, 10**10 + 1, 2026):
    if fnmatch(str(N), '431*7?14'):
        print(N, N // 2026)