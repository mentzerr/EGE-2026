with open('26_4660.txt') as file:
    N = int(file.readline())
    prices = sorted([int(x) for x in file])

disc_prices = N // 4

price_one_check = sum(prices) - sum(prices[:disc_prices]) // 2
price_diff_check = sum(prices) - sum(prices[::-1][3::4]) // 2

print(price_one_check, price_diff_check)




