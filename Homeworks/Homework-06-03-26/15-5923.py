from itertools import combinations

def f(x):
    P = 5 <= x <= 280
    Q = 295 <= x <= 400
    R = 375 <= x <= 450
    A = A1 <= x <= A2
    return (Q <= P) or ((not A) <= R)

line_A = [5, 280, 295, 375, 400, 450]
line_X = [5.5, 280.5, 295.5, 375.5, 400.5]

ans = []
for A1, A2 in combinations(line_A, 2):
    if all(f(x) for x in line_X):
        ans.append(A2 - A1)
print(min(ans))