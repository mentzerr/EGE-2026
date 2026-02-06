def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0: return False
    return True

def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2

    i = 3
    while i**2 < num:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 2:
        d += [num]
    return d

k = 0
for N in range(5_000_001, 10**10, 2):
    D = fact(N)
    if len(D) == len(set(D)) == 2 and is_prime(abs(D[0] - D[1])):
        print(N, max(D))
        k += 1
        if k == 5:
            break
            



