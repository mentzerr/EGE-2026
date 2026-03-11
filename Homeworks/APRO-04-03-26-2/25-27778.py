from fnmatch import fnmatch

for N in range(1200156 - 1200156 % 271, 10**8 + 1, 271):
    if fnmatch(str(N), '12??15*6'):
        print(N, N // 271)
