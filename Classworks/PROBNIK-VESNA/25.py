def div(num):
    d = set()

    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            if str(i)[-2:] == '11' and i != 11: d |= {i}
            if str(num // i)[-2:] == '11' and (num // i) != 11: d |= {num // i}

    if len(d) > 0:
        return min(d)
    return 0

cnt = 0
for N in range(1_350_051, 10**9):
    if M := div(N):
        print(N, M)
        cnt += 1
        if cnt == 5:
            break
