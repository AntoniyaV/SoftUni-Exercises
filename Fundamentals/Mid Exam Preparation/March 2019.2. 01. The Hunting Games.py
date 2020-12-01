days = int(input())
players = int(input())
energy = float(input())

water_per_day_per_person = float(input())
food_per_day_per_person = float(input())

total_water = water_per_day_per_person * days * players
total_food = food_per_day_per_person * days * players

for day in range(1, days + 1):
    energy_lost = float(input())
    energy -= energy_lost
    if energy <= 0:
        break

    if day % 2 == 0:
        energy += 0.05 * energy
        total_water *= 0.7

    if day % 3 == 0:
        energy += 0.1 * energy
        total_food -= total_food / players

if energy > 0:
    print(f"You are ready for the quest. You will be left with - {energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
