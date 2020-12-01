gifts = input()
list_gifts = gifts.split()
command = ""

while not command == "No Money":
    command = input()
    split_command = command.split()
    if "OutOfStock" in command:
        while split_command[1] in list_gifts:
            pos = list_gifts.index(split_command[1])
            list_gifts[pos] = "None"
    elif "Required" in command:
        command_index = int(split_command[2])
        if command_index in range(len(list_gifts)):
            list_gifts[command_index] = split_command[1]
    elif "JustInCase" in command:
        list_gifts[-1] = split_command[1]

for el in list_gifts:
    if not el == "None":
        print(el, end=" ")
