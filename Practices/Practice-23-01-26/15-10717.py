def T(n, m, k):
    return n+m > k and k+n > m and m+k > n

def f(x):
    return not(T(x, 11, 18) == (not(max(x, 5) > 68)) and T(x, A, 5))

for A in range(1, 1000)[::-1]:
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break


