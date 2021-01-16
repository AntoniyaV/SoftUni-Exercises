items = input().split("|")
budget = float(input())

bought_items = []

for item in items:
    item_type, item_price = item.split("->")
    item_price = float(item_price)

    if (item_type == "Clothes" and item_price <= 50.00) \
            or (item_type == "Shoes" and item_price <= 35.00) \
            or (item_type == "Accessories" and item_price <= 20.50):

        if budget >= item_price:
            budget -= item_price
            bought_items.append(item_price)

new_prices = list(map(lambda x: (x * 0.4) + x, bought_items))
new_prices_str = [str(round(price, 2)) for price in new_prices]

result = " ".join(new_prices_str)
profit = round(0.4 * sum(bought_items), 2)
new_budget = budget + sum(new_prices)

print(result)
print(f"Profit: {profit}")

if new_budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
