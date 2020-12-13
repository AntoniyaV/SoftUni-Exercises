command = input()

guests = {}
unliked_meals = 0

while not command == "Stop":
    action, guest, meal = command.split("-")

    if action == "Like":
        if guest not in guests:
            guests[guest] = []

        if meal not in guests[guest]:
            guests[guest].append(meal)

    elif action == "Unlike":
        if guest in guests:
            if meal in guests[guest]:
                unliked_meals += 1
                guests[guest].remove(meal)
                print(f"{guest} doesn't like the {meal}.")

            else:
                print(f"{guest} doesn't have the {meal} in his/her collection.")

        else:
            print(f"{guest} is not at the party.")

    command = input()

sorted_guests = dict(sorted(guests.items(), key=lambda x: (-len(x[1]), x[0])))

for sorted_guest, meals in sorted_guests.items():
    print(f"{sorted_guest}: {', '.join(meals)}")

print(f"Unliked meals: {unliked_meals}")