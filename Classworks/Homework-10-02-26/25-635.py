def f(num):
    d = set()
    for i in range(2, int(num **.5) + 1):
        if num % i == 0:
            d |= {num // i, i}

    if len(d) == 3:
        return d
    return []

for N in range(int(106_732_567**.5), int(152_673_837 ** .5)):
    if M := f(N ** 2):
        print(N ** 2, max(M))

