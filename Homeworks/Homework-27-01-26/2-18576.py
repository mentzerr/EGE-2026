from itertools import product, permutations

def f(x,y,w,z):
    return not(w <= (x == y)) and (z <= x)

for x1,x2,x3,x4,x5 in product([0, 1], repeat = 5):
    t = (
        (x1,1,1,x2,1),
        (0,x3,x4,0,1),
        (x5,0,1,0,1)
    )
    if len(t) == len(set(t)):
        for p in permutations('xywz', r=4):
            if all(f(**dict(zip(p, line))) == line[-1] for line in t):
                print(*p)