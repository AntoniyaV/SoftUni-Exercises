money_needed = float(input())
money_owned = float(input())

days_count = 0
days_spend_count = 0
saved = True

while money_owned < money_needed:
    action = input()
    money_action = float(input())
    days_count += 1
    if action == "spend":
        money_owned -= money_action
        if money_owned < 0:
            money_owned = 0
        days_spend_count += 1
    elif action == "save":
        money_owned += money_action
        days_spend_count = 0
    if days_spend_count == 5:
        saved = False
        break

if saved:
    print(f"You saved the money for {days_count} days.")
else:
    print("You can't save the money.")
    print(f"{days_count}")