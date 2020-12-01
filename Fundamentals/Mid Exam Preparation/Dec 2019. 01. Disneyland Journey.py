journey_cost = float(input())
months = int(input())

saved_money = 0

for month in range(1, months + 1):
    if not month == 1 and not month % 2 == 0:
        saved_money -= 0.16 * saved_money

    if month % 4 == 0:
        bonus = 0.25 * saved_money
        saved_money += bonus

    saved_money += 0.25 * journey_cost

if saved_money >= journey_cost:
    print(f"Bravo! You can go to Disneyland and you will have {saved_money - journey_cost:.2f}lv. for souvenirs.")

else:
    print(f"Sorry. You need {journey_cost - saved_money:.2f}lv. more.")