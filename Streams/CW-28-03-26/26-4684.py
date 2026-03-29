with open('26_4684.txt') as file:
    N = int(file.readline())
    prices = sorted([int(x) for x in file])

discounted_prices = N // 6

one_check_prices = sum(prices) - sum(prices[:discounted_prices]) // 2
diff_check_prices = sum(prices) - sum(prices[::-1][5::6]) // 2

print(one_check_prices, diff_check_prices)

