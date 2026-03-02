from itertools import product, permutations


def f(x, y, w, z):
    return not (((not x) or y) and (not w)) or (not (z and (not (y and w))))


for x1, x2, x3, x4, x5, x6, x7 in product([0, 1], repeat=7):
    t = (
        (0, x1, x2, 1, 0),
        (x3, 1, x4, x5, 0),
        (1, 0, x6, x7, 0)
    )
    if len(t) == len(set(t)):
        for p in permutations('xywz'):
            if all(f(**dict(zip(p, line))) == line[-1] for line in t):
                print(*p, sep='')
