stops = input()
command = input()

while not command == "Travel":
    action, item_one, item_two = command.split(":")

    if action == "Add Stop":
        index = int(item_one)
        string = item_two

        if index in range(len(stops)):
            stops = stops[:index] + string + stops[index:]

    elif action == "Remove Stop":
        start_index, end_index = int(item_one), int(item_two)

        if start_index in range(len(stops)) and end_index in range(len(stops)):
            stops = stops[:start_index] + stops[end_index + 1:]

    elif action == "Switch":
        old_string, new_string = item_one, item_two

        if old_string in stops:
            stops = stops.replace(old_string, new_string)

    print(stops)

    command = input()

print(f"Ready for world tour! Planned stops: {stops}")