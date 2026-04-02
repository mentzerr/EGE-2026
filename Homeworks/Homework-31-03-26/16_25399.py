F = [0] * 2600
G = [0] * 333_333

for j in range(333_000, 0, -1):
    if j > 303_728: G[j] = j - 15
    else: G[j] = G[j + 8] / 2 - 109

for i in range(0, 2600):
    if i >= 128: F[i] = F[i - 5] + 1092
    else: F[i] = 5 * G[i - 7] + 29



print(F[2048])