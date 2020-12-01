days = int(input())
hours = int(input())

price = 0

for i in range(1, days + 1):
    price_day = 0

    for j in range(1, hours + 1):
        if i % 2 == 0 and j % 2 != 0:
            price_day += 2.5
        elif i % 2 != 0 and j % 2 == 0:
            price_day += 1.25
        else:
            price_day += 1

    price += price_day
    print(f"Day: {i} - {price_day:.2f} leva")

print(f"Total: {price:.2f} leva")