file = open('9_24070')

k = 0
for s in file:
    a = [int(x) for x in s.split()]
    if len(set(a)) == len(a) and max(a) + min(a) <= sum(a) - (max(a) + min(a)):
        k += 1
print(k)