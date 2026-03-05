from itertools import permutations

graph = 'AF FE EB BD DA CE CB CA'.split()
matrix = '36 456 145 236 23 124'.split()
print(*range(1, 7))

for i in permutations('ABCDEF'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i) # 27 + 18 = 45