items = input().split("|")
budget = float(input())

money_spent = 0.00
sum_new_prices = 0.00
new_prices = ""

for pair in items:
    item_type, item_price = pair.split("->")
    item_price = float(item_price)
    new_price = 0.00

    if (item_type == "Clothes" and item_price <= 50.00) \
            or (item_type == "Shoes" and item_price <= 35.00) \
            or (item_type == "Accessories" and item_price <= 20.50):

        if budget >= item_price:
            budget -= item_price
            new_price = item_price + 0.4 * item_price
            new_prices += f"{new_price:.2f} "

            money_spent += item_price
            sum_new_prices += new_price

print(new_prices.rstrip())
print(f"Profit: {money_spent * 0.4:.2f}")

if sum_new_prices + budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
