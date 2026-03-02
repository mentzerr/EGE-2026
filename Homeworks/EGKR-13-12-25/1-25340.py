from itertools import permutations

graph = 'AC CB BH HD DA FH FE GE GC GA'.split()
matrix = '368 34 126 27 67 135 458 17'.split()
print(*range(1, 9))

for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i) # 15 + 13 = 28