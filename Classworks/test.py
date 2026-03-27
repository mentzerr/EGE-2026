a = [1, 3, 4, 5]
b = [3, 4, 6]
new_list = [x for x in a if x not in b]
print(new_list, len(a), len(a) - len(new_list))