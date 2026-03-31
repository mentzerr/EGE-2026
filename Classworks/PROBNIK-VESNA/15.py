from itertools import combinations
def f(x):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = A1 <= x <= A2
    return P <= ((Q and (not A)) <= (not P))

line_A = [15, 21, 40, 63]
line_X = [15.5, 21.5, 40.5]

ans = []
for A1, A2 in combinations(line_A, 2):
    if all(f(x) for x in line_X):
        ans.append(A2 - A1)
print(min(ans))
