# from functools import lru_cache
#
# @lru_cache(None)
# def Q(n): # 11240 -> 20
#     if n < 21: return n + 4
#     return Q(n - 4) + 2
#
# @lru_cache(None)
# def G(n): # 46 -> 11240
#     if n < 11240: return G(n + 3) + 2
#     return Q(n)
#
# @lru_cache(None)
# def F(n): # 2026 -> 42
#     if n < 43: return G(n + 4)
#     return 2 * F(n - 2) - F(n - 4) + 2
#
# for k in range(21, 11_240):
#     Q(k)
# for j in range(11_240, 46, -1):
#     G(j)
#
# print(F(2026))

############################################

F = [0] * 2_500
G = [0] * 12_000
Q = [0] * 12_000

for i in range(0, 12_000):
    if i < 21: Q[i] = i + 4
    else: Q[i] = Q[i - 4] + 2

for i in range(1, 12_000)[::-1]:
    if i < 11_240: G[i] = G[i + 3] + 2
    else: G[i] = Q[i]

for i in range(1, 2_500):
    if i < 43: F[i] = G[i + 4]
    else: F[i] = 2 * F[i - 2] - F[i - 4] + 2

print(F[2026])
