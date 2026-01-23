from re import *

with open(r'./Files/24_1874.txt') as file:
    data = file.readline()

data = '*****Q*******W****QW*********'

pattern = r'[^Q]+[^W]'
matches = [match.group() for match in finditer(pattern, data)]
print(matches)
