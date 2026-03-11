from itertools import product, permutations


def f(x, y, w, z):
    return (not z and y and x and not w) or (not z and y and not x and not w) or (z and y and x and not w)


for x1, x2, x3, x4, x5, x6, x7 in product([0, 1], repeat=7):
    t = (
        (x1, 1, x2, x3, 1),
        (x4, 0, 1, x5, 1),
        (0, x6, 0, x7, 1)
    )
    if len(t) == len(set(t)):
        for p in permutations('xywz'):
            if all(f(**dict(zip(p, line))) == line[-1] for line in t):
                print(*p, sep='')
