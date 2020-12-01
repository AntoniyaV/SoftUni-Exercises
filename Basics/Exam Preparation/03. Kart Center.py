money = float(input())
rounds = input()
fan_card = input()
type_cart = input()

ticket_price = 0

if rounds == "five":
    if type_cart == "Child":
        ticket_price = 7
    elif type_cart == "Junior":
        ticket_price = 9
    elif type_cart == "Adult":
        ticket_price = 12
    elif type_cart == "Profi":
        ticket_price = 18

else:
    if type_cart == "Child":
        ticket_price = 11
    elif type_cart == "Junior":
        ticket_price = 16
    elif type_cart == "Adult":
        ticket_price = 21
    elif type_cart == "Profi":
        ticket_price = 32


if fan_card == "yes":
    ticket_price -= (ticket_price * 0.20)

if ticket_price <= money:
    print(f"You bought {type_cart} ticket for {rounds} laps. Your change is {money - ticket_price:.2f}lv.")
else:
    print(f"You don't have enough money! You need {ticket_price - money:.2f}lv more.")