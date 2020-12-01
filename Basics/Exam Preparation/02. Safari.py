budget = float(input())
litres = float(input())
day = input()

total_price = litres * 2.10 + 100
discount = 0

if day == 'Saturday':
    discount = total_price * 0.1
else:
    discount = total_price * 0.2

total_price -= discount

if budget >= total_price:
    print(f"Safari time! Money left: {budget - total_price:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {total_price - budget:.2f} lv.")