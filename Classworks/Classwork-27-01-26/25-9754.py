from fnmatch import fnmatch

for N in range(30157, 10**8+1, 2023):
    if fnmatch(str(N), '3?1*57') and N % 2023:
        print(N, N//2023)
        