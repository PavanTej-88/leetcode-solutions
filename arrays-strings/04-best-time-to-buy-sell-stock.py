def max_profit(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)

    return max_profit


# Typical test case
prices = [7, 1, 5, 3, 6, 4]

result = max_profit(prices)
print("Typical test case:", result)


# Edge case
prices = [7, 6, 4, 3, 1]

result = max_profit(prices)
print("Edge case:", result)