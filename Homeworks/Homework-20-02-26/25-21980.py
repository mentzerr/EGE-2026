def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0: return False
    return True

def divisor(num):
    d = set()
    for j in range(2, int(num ** .5) + 1):
        if num % j == 0:
            if is_prime(j) and j % 10 == 7: d |= {j}
            if is_prime(num // j) and num // j % 10 == 7: d |= {num // j}

    if len(d) > 1:
        return sum(d) // len(d)
    return 0

k = 0
for N in range(749_999, 0, -1):
    F = divisor(N)
    if F % 111 == 0 and F != 0:
        print(N, F)
        k += 1
        if k == 5:
            break
