command = input()
products = {}

while not command == "buy":
    name, price, quantity = command.split()
    price, quantity = float(price), int(quantity)

    if name not in products:
        products[name] = [price, quantity]

    else:
        products[name][0] = price
        products[name][1] += quantity

    command = input()

for product, value in products.items():
    print(f"{product} -> {value[0] * value[1]:.2f}")
