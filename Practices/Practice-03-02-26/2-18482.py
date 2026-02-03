from itertools import product, permutations


def f(x, y, w, z):
    return (x == (y <= (z or x))) and w


for x1, x2, x3, x4, x5 in product([0, 1], repeat=5):
    t = (
        (1, 0, 1, x1, 1),
        (0, x2, x3, 0, 1),
        (1, 0, x4, x5, 1)
    )
    if len(t) == len(set(t)):
        for p in permutations('xywz'):
            if all(f(**dict(zip(p, line))) == line[-1] for line in t):
                print(*p)
