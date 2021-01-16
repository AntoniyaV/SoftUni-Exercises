collection_of_items = input()
budget = float(input())

items = collection_of_items.split("|")
money_spent = 0.00
sum_new_prices = 0.00

for pair in items:
    pair_split = pair.split("->")
    item_type = pair_split[0]
    item_price = float(pair_split[1])
    new_price = 0.00

    if (item_type == "Clothes" and item_price <= 50.00) \
        or (item_type == "Shoes" and item_price <= 35.00) \
        or (item_type == "Accessories" and item_price <= 20.50):

        budget -= item_price
        if budget >= 0:
            new_price = item_price + 0.4 * item_price
            print(f"{new_price:.2f}", end=" ")

            money_spent += item_price
            sum_new_prices += new_price
        else:
            budget += item_price
            continue

print()
print(f"Profit: {money_spent * 0.4:.2f}")

if sum_new_prices + budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
