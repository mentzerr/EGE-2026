file = open('4')

k = 0
for s in file:
    a = [int(x) for x in s.split()]
    raz_a = [x for x in a if a.count(x) == 1]
    max_a = [x for x in a if x == max(a) and 3 <= a.count(x) <= 4]
    raz_a1 = [x for x in raz_a if max(raz_a) + min(raz_a) <= (sum(raz_a) - (max(raz_a) + min(raz_a)))]
    if max_a and raz_a1:
        k += 1
print(k)
