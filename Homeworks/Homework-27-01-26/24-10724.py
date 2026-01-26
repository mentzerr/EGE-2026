from re import *
with open(r'../Homework-27-01-26/24_10724.txt') as file:
    data = file.readline()

pattern = '[^0|G-Z]+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))