file = open('3')

k = 0
for s in file:
    a = [int(x) for x in s.split()]
    a1 = [int(x) for x in a if sorted(a) == a]
    a_ch = [int(x) for x in a if int(x) % 2 == 0]
    a_nch = [int(x) for x in a if int(x) % 2 == 1]
    if len(a1) == 7 and len(a_ch) > len(a_nch):
        k += 1
print(k)
