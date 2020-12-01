days = int(input())
budget = float(input())
people = int(input())
fuel_per_km = float(input())
food_person_day = float(input())
hotel_person_night = float(input())

total_food = food_person_day * people * days
total_hotel = hotel_person_night * people * days
if people > 10:
    total_hotel *= 0.75

current_expenses = total_food + total_hotel

for day in range(1, days + 1):
    current_distance = float(input())

    current_fuel = current_distance * fuel_per_km
    current_expenses += current_fuel

    if day % 3 == 0 or day % 5 == 0:
        current_expenses += 0.4 * current_expenses
    if day % 7 == 0:
        current_expenses -= current_expenses / people

    if current_expenses > budget:
        print(f"Not enough money to continue the trip. You need {current_expenses - budget:.2f}$ more.")
        break

if current_expenses <= budget:
    print(f"You have reached the destination. You have {budget - current_expenses:.2f}$ budget left.")