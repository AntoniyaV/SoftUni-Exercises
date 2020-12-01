total_price = 0
command = ""

while True:
    command = input()
    if command == "special" or command == "regular":
        break

    price = float(command)
    if price <= 0:
        print("Invalid price!")
    else:
        total_price += price

taxes = total_price * 0.2
total_with_taxes = total_price + taxes

if not total_price == 0:
    if command == "special":
        total_with_taxes *= 0.9

    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_with_taxes:.2f}$")

else:
    print("Invalid order!")

