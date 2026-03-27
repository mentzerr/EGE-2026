from re import *

with open(r'../Files/24_26077.txt') as file:
    data = file.readline()

pattern = r'G([^13579G]*[13579]){45}[^13579G]*'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key = len)))


for i in '13579':
    data = data.replace(i, '*')

data = data.split('G')

ans = 0
for line in data:
    if line.count('*') == 45:
        ans = max(ans, len(line) + 1)
    elif line.count('*') > 45:
        while line.count('*') > 45:
            line = line[:line.rfind('G')]
        ans = max(ans, len(line) + 1)

print(ans)

