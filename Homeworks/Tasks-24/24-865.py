from re import *

with open(r'./Files/24_865.txt') as file:
    data = file.readline()

pattern = '[^CF]+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))