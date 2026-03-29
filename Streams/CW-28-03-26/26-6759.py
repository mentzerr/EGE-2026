with open('26_6759.txt') as file:
    N = int(file.readline())
    prices = sorted([int(x) for x in file])

discounted_price = N // 3

first_way_check = sum(prices) - sum(prices[-discounted_price:])
second_way_check = sum(prices) - sum(prices[::-1][2::3])

print(first_way_check)
print(second_way_check)