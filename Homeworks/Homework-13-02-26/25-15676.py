from fnmatch import fnmatch

def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0: return True
    return False

for NUM in range(14036 - 14036 % 22768, 10**8, 22768):
    for x in range(1, 1000):
        if is_prime(x):
            if fnmatch(str(NUM), f'1{x}03*6*'):
                print(NUM, x)