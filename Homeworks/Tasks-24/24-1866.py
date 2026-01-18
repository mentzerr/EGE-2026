### Через цикл

# with open(r'.\Files\24_1866.txt') as file:
#     data = file.readline()
#
# ans = 0
# k = 1
# for i in range(len(data) - 1):
#     if data[i] + data[i + 1] not in 'ada':
#         k += 1
#     else:
#         ans = max(ans, k)
#         k = 1
# ans = max(ans, k)
# print(ans)

### Через замены
#
# with open(r'./Files/24_1866.txt') as file:
#     data = file.readline()
#
# data = data.replace('ad', 'a d')
# data = data.replace('da', 'd a')
# data = data.split()
# print(len(max(data, key=len)))

### Через регулярные выражения

from re import *

with open(r'./Files/24_1866.txt') as file:
    data = file.readline()

pattern = r'(?<=(ad|da)).+?(?=(ad|da))'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) + 2)