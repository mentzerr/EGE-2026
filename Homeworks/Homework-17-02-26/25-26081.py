def f(num):
    for i1 in range(113, num, 226):
        for i2 in range(0, 13): # степень двойки, что < 1_000_000
            if i1 + 3 ** i2 == num:
                return i2
    return 0


k = 0
for N in range(111_112, 1_000_000, 2): # N = нечет + нечет = чет
    if S := f(N):
        if '0' not in str(N):
            print(N, S)
            k += 1
            if k == 5:
                break

