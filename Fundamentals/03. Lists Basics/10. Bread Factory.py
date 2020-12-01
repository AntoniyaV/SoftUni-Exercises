str_events = input()
events = str_events.split("|")

energy = 100
coins = 100
managed = True

for evnt in events:
    event = evnt.split("-")
    name_or_ingredient = event[0]
    number = int(event[1])

    if name_or_ingredient == "rest":
        if energy + number > 100:
            number = 0
        else:
            energy += number
        print(f"You gained {number} energy.")
        print(f"Current energy: {energy}.")

    elif name_or_ingredient == "order":
        if energy - 30 >= 0:
            energy -= 30
            coins += number
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins - number > 0:
            coins -= number
            print(f"You bought {name_or_ingredient}.")
        else:
            managed = False
            print(f"Closed! Cannot afford {name_or_ingredient}.")
            break

if managed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
