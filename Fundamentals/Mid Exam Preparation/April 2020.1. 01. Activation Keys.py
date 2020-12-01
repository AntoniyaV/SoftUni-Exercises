activation_key = input()
command = input()

while not command == "Generate":
    if "Contains" in command:
        substring = command.split(">>>")[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif "Flip" in command:
        activation_key = list(activation_key)
        subcommand = command.split(">>>")[1]
        start_index = int(command.split(">>>")[2])
        end_index = int(command.split(">>>")[3])
        new_substring = []

        for el in activation_key[start_index:end_index]:
            if el.isalpha() and subcommand == "Upper":
                el = el.upper()
            elif el.isalpha() and subcommand == "Lower":
                el = el.lower()
            new_substring.append(el)

        new_key = activation_key[:start_index] + new_substring + activation_key[end_index:]
        activation_key = "".join(new_key)
        print(activation_key)

    elif "Slice" in command:
        activation_key = list(activation_key)
        start_index = int(command.split(">>>")[1])
        end_index = int(command.split(">>>")[2])

        new_key = activation_key[:start_index] + activation_key[end_index:]
        activation_key = "".join(new_key)
        print(activation_key)

    command = input()

print(f"Your activation key is: {activation_key}")
