from re import *

with open(r'../Tasks-24/Files/24_19254.txt') as file:
    data = file.readline()



pattern = r'123123123'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key = len)))