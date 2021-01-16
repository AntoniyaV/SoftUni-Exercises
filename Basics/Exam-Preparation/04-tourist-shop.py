budget = float(input())
product_count = 0
total_price = 0

while True:
    product_name = input()
    if product_name == "Stop":
        break

    product_price = float(input())

    product_count += 1
    if product_count % 3 == 0:
        product_price = product_price / 2

    if product_price > budget:
        break

    budget -= product_price
    total_price += product_price

if product_price > budget:
    print("You don't have enough money!")
    print(f"You need {product_price - budget:.2f} leva!")
else:
    print(f"You bought {product_count} products for {total_price:.2f} leva.")