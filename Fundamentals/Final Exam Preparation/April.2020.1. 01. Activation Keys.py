def flip_chars(some_command, some_key):
    case = some_command.split(">>>")[1]
    start, end = int(some_command.split(">>>")[2]), int(some_command.split(">>>")[3])
    change_case = ""

    if case == "Upper":
        change_case = some_key[start:end].upper()
    elif case == "Lower":
        change_case = some_key[start:end].lower()

    some_key = some_key[:start] + change_case + some_key[end:]

    return some_key


def slice_substring(some_command, some_key):
    start, end = int(some_command.split(">>>")[1]), int(some_command.split(">>>")[2])
    some_key = some_key[:start] + some_key[end:]

    return some_key


raw_activation_key = input()
command = input()

while not command == "Generate":
    action = command.split(">>>")[0]

    if action == "Contains":
        substring = command.split(">>>")[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif action == "Flip":
        raw_activation_key = flip_chars(command, raw_activation_key)
        print(raw_activation_key)

    elif action == "Slice":
        raw_activation_key = slice_substring(command, raw_activation_key)
        print(raw_activation_key)

    command = input()

print(f"Your activation key is: {raw_activation_key}")