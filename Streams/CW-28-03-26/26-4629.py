with open('26_4629.txt') as file:
    N = int(file.readline())
    prices = sorted([int(x) for x in file])

prices_with_dis = N // 4

buyer = sum(prices) - sum(prices[-prices_with_dis:]) // 2
store = sum(prices) - sum(prices[:prices_with_dis]) // 2

print(buyer, store)

