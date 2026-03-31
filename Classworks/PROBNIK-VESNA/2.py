from itertools import product, permutations


def f(x, y, w, z):
    return ((z == x) <= w) and (w <= (y and x))


for x1, x2, x3 in product([0, 1], repeat=3):
    t = (
        (1, 1, x1, 0, 1),
        (1, x2, x3, 0, 1),
        (1, 0, 1, 1, 1)
    )
    if len(t) == len(set(t)):
        for p in permutations('xywz'):
            if all(f(**dict(zip(p, line))) == line[-1] for line in t):
                print(*p, sep = '')
