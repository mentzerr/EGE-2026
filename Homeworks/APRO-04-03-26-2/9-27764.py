file = open('9_27764')

k = 0

for s in file:
    a = sorted([int(x) for x in s.split()])
    if len(a) == len(set(a)) and \
        2*(a[0] + a[-1]) == sum(a[1:-1]):
        k += 1
print(k)