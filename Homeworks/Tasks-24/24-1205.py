### Через цикл

# with open(r'./Files/24_1205.txt') as file:
#     data = file.readline()
#
# ans = 0
# k = 0
# for i in data:
#     if i not in 'GWP':
#         k += 1
#     else:
#         ans = max(ans, k)
#         k = 0
# ans = max(ans, k)
# print(ans)

### Через замены
#
# with open(r'./Files/24_1205.txt') as file:
#     data = file.readline()
#
# for i in 'GWP':
#     data = data.replace(i, ' ')
# data = data.split()
# print(len(max(data, key=len)))

### Через регулярные выражения

from re import *

with open(r'./Files/24_1205.txt') as file:
    data = file.readline()

pattern = r'[^GWP]+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))