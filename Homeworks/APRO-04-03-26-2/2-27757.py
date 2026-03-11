from itertools import product, permutations


def f(x, y, w, z):
    return (not x and y and z and not w) or (not x and y and not z and not w) \
        or (x and y and z and not w)


for x1, x2, x3, x4, x5, x6, x7 in product([0, 1], repeat=7):
    t = (
        (1, x1, x2, x3, 1),
        (0, x4, 1, x5, 1),
        (x6, 0, 0, x7, 1)
    )
    if len(t) == len(set(t)):
        for p in permutations('xywz'):
            if all(f(**dict(zip(p, line))) == line[-1] for line in t):
                print(*p, sep='')