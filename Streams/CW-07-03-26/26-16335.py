with open('26_16335.txt') as file:
    N = int(file.readline())
    forms = sorted([int(i) for i in file], reverse = True)

last_picked_korzh = forms[0]
k = 1

for korzh in forms:
    if last_picked_korzh - korzh >= 4:
        last_picked_korzh = korzh
        k += 1
print(k, last_picked_korzh)