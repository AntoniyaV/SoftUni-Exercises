def target_manipulations(some_command, list_of_targets):
    action, index, value = some_command.split()
    index, value = int(index), int(value)

    if action == "Shoot":
        if 0 <= index < len(list_of_targets):
            list_of_targets[index] -= value
            if list_of_targets[index] <= 0:
                list_of_targets.pop(index)

    elif action == "Add":
        if 0 <= index < len(list_of_targets):
            list_of_targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        if 0 <= index < len(list_of_targets) \
                and 0 <= index - value < len(list_of_targets) \
                and 0 <= index + value < len(list_of_targets):
            del list_of_targets[index - value:index + value + 1]
        else:
            print("Strike missed!")

    return list_of_targets


targets = input().split()
command = input()

targets = list(map(lambda n: int(n), targets))

while not command == "End":
    targets = target_manipulations(command, targets)
    command = input()

result = [str(i) for i in targets]
print("|".join(result))
