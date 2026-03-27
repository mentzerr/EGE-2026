with open('9_17863') as file:
    k = 0
    for s in file:
        data = [int(x) for x in s.split()]
        data_p = [x for x in data if data.count(x) == 3]
        data_ost = [x for x in data if x not in data_p]
        if len(data_p) == 3 and len(data_ost) == 3 == len(set(data_ost)):
            if sum(data_p) ** 2 > sum(data_ost) ** 2:
                k += 1
print(k)