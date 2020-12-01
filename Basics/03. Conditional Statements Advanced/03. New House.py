flowers = input()
number = int(input())
budget = int(input())
price = 0

if flowers == "Roses":
    price = number * 5
    if number > 80:
        price -= price * 0.10
elif flowers == "Dahlias":
    price = number * 3.80
    if number > 90:
        price -= price * 0.15
elif flowers == "Tulips":
    price = number * 2.80
    if number > 80:
        price -= price * 0.15
elif flowers == "Narcissus":
    price = number * 3
    if number < 120:
        price += price * 0.15
elif flowers == "Gladiolus":
    price = number * 2.50
    if number < 80:
        price += price * 0.20

if price <= budget:
    print(f"Hey, you have a great garden with {number} {flowers} and {budget - price:.2f} leva left.")
else:
    print(f"Not enough money, you need {price - budget:.2f} leva more.")