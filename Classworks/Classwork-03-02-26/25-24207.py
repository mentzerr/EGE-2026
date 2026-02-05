def is_prime(num):
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return [i] + is_prime(num // i)
    return[num]

k = 0
for N in range(24_517_513, 10**9):
    if len(is_prime(N)) == 12:
        F = is_prime(N)
        print(N, max(F))
        k += 1
        if k == 5:
            break