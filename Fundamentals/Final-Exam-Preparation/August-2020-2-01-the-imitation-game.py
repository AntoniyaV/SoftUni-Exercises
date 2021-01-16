message = input()
command = input()

while not command == "Decode":
    action = command.split("|")[0]

    if action == "Move":
        num_letters = int(command.split("|")[1])
        message = message[num_letters:] + message[:num_letters]

    elif action == "Insert":
        index, value = int(command.split("|")[1]), command.split("|")[2]
        message = message[:index] + value + message[index:]

    elif action == "ChangeAll":
        substring, replacement = command.split("|")[1], command.split("|")[2]
        message = message.replace(substring, replacement)

    command = input()

print(f"The decrypted message is: {message}")