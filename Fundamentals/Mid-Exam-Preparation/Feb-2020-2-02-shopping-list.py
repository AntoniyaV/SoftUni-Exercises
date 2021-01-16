def add_urgent(some_command, groceries_list):
    action, item = some_command.split()
    if item not in groceries_list:
        groceries_list.insert(0, item)
    return groceries_list


def remove_unnecessary(some_command, groceries_list):
    action, item = some_command.split()
    if item in groceries_list:
        groceries_list.remove(item)
    return groceries_list


def correct_item(some_command, groceries_list):
    action, old_item, new_item = some_command.split()
    if old_item in groceries_list:
        index = groceries_list.index(old_item)
        groceries_list[index] = new_item
    return groceries_list


def rearrange_item(some_command, groceries_list):
    action, item = some_command.split()
    if item in groceries_list:
        groceries_list.remove(item)
        groceries_list.append(item)
    return groceries_list


groceries = input().split("!")
command = input()

while not command == "Go Shopping!":
    if "Urgent" in command:
        groceries = add_urgent(command, groceries)
    elif "Unnecessary" in command:
        groceries = remove_unnecessary(command, groceries)
    elif "Correct" in command:
        groceries = correct_item(command, groceries)
    elif "Rearrange" in command:
        groceries = rearrange_item(command, groceries)

    command = input()

print(', '.join(groceries))