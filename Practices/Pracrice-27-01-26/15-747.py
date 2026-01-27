from itertools import combinations

def f(x):
    P = 43 <= x <= 49
    Q = 44 <= x <= 53
    A = A1 <= x <= A2
    return (A <= P) or Q

line_A = [43, 44, 49, 53]
line_X = [43.5, 47, 51]

ans = []
for A1, A2 in combinations(line_A, 2):
    if all(f(x) for x in line_X):
        ans.append(A2 - A1)
print(max(ans))