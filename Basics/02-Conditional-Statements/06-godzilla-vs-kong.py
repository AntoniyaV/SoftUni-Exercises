budget = float(input())
statics = int(input())
price_clothes = float(input())
decor = budget * 0.1
clothes = statics * price_clothes
if statics > 150:
    clothes = clothes - (clothes * 0.1)
    total = decor + clothes
    if total > budget:
        print("Not enough money!")
        print(f"Wingard needs {total - budget:.2f} leva more.")
    elif total <= budget:
        print("Action!")
        print(f"Wingard starts filming with {budget - total:.2f} leva left.")
else:
    total = decor + clothes
    if total > budget:
        print("Not enough money!")
        print(f"Wingard needs {total - budget:.2f} leva more.")
    elif total <= budget:
        print("Action!")
        print(f"Wingard starts filming with {budget - total:.2f} leva left.")