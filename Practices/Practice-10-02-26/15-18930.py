from itertools import combinations
def f(x):
    P = 10 <= x <= 150
    Q = 160 <= x <= 250
    R = 240 <= x <= 300
    A = A1 <= x <= A2
    return (Q <= P) or ((not A) <= R)

line_A= [10, 150, 160, 240, 250, 300]
line_X = [10.5, 150.5, 160.5, 240.5, 250.5]

ans = []
for A1, A2 in combinations(line_A, 2):
    if all(f(x) for x in line_X):
        ans.append(A2 - A1)
print(min(ans))
