items = input().split(", ")
command = input()

while not command == "Craft!":
    action, item = command.split(" - ")

    if action == "Collect":
        if item not in items:
            items.append(item)

    elif action == "Drop":
        if item in items:
            items.remove(item)

    elif action == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in items:
            index = items.index(old_item) + 1
            items.insert(index, new_item)

    elif action == "Renew":
        if item in items:
            items.append(item)
            items.remove(item)

    command = input()

result = ", ".join(items)
print(f"{result}")
