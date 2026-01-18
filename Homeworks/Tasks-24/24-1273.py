### Через цикл

# with open(r'./Files/24_1273.txt') as file:
#     data = file.readline()
#
# ans = 0
# k = 2
# for i in range(len(data) - 2):
#     if data[i] + data[i + 1] + data[i + 2] != 'XYZ':
#         k += 1
#     else:
#         ans = max(ans, k)
#         k = 2
# ans = max(ans, k)
# print(ans)

### Через замены
#
# with open(r'./Files/24_1273.txt') as file:
#     data = file.readline()
#
# while 'XYZ' in data:
#     data = data.replace('XYZ', 'XY YZ')
# data = data.split()
# print(len(max(data, key=len)))

### Через регулярные выражения
from re import *

with open(r'./Files/24_1273.txt') as file:
    data = file.readline()

pattern = r'(?<=XYZ).+?(?=XYZ)'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) + 4)
