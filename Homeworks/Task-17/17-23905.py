def check1(n, m):
    return n > m

def check2(n):
    return str(n)[-1] == str(n)[-2]

def check3(list):
    summary = 0
    for i in list:
        for j in i:
            if str(j)[-1] == str(j)[-2]:
                summary += j

    return summary

a = [int(x) for x in open('17_23905.txt')]

max_el = max([x for x in a if x % 100 == 37])

ans = []

for x, y, w, z in zip(a, a[1:], a[2:], a[3:]):
    if check1(x, max_el) + check1(y, max_el) + check1(w, max_el) + check1(z, max_el) == 2:
        if check2(x) + check2(y) + check2(z) + check2(w) == 1:
            ans.append([x, y, w, z])
print(len(ans), check3(ans))