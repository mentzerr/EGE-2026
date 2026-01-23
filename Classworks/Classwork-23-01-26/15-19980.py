from itertools import combinations

def f(x):
    P = 52 <= x <= 105
    Q = 0 <= x <= 53
    A = A1 <= x <= A2
    return (not P and not Q and not A) <= (x**2 > 303601)

line_A = [0, 52, 53, 105]
line_X = [20, 52.5, 90]

ans = []
for A1, A2 in combinations(line_A, 2):
    if all(f(x) for x in line_X):
        ans.append(A2-A1)
print(min(ans))