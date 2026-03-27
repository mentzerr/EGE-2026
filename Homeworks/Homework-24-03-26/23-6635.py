def f(start, step):
    if step == 13:
        if start < 0:
            return {start}
        return set()

    return f(start - 3, step + 1) | f(start * -3, step + 1)
print(len(f(333, 0)))