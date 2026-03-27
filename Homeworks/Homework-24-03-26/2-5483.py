from itertools import product, permutations


def f(x, y, w, z):
    return (z == (not x)) <= ((w <= (not y)) and (y <= x))


for x1, x2, x3, x4, x5 in product([0, 1], repeat=5):
    t = (
        (1, 1, 1, 0, 1),
        (x1, x2, 0, 0, 0),
        (x3, 0, x4, x5, 0)
    )
    if len(t) == len(set(t)):
        for p in permutations('xywz'):
            if all(f(**dict(zip(p, line))) == line[-1] for line in t):
                print(*p, sep = '')
