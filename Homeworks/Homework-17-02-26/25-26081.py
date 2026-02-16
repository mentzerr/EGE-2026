for N in range(111_111, 1_000_000):
    for NUM in range(1, 100):
        if '0' not in str(N) and N == 3 ** (NUM) + N:
            if N % 113 == 0 and N % 2 == 1:
                print(N)
                break
