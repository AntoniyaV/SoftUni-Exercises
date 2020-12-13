message = input()
command = input()

while not command == "Reveal":
    action, substr = command.split(":|:")[0], command.split(":|:")[1]

    if action == "InsertSpace":
        index = int(substr)
        message = message[:index] + " " + message[index:]
        print(message)

    elif action == "Reverse":
        if substr not in message:
            print("error")
        else:
            message = message.replace(substr, '', 1)
            message += substr[::-1]
            print(message)

    elif action == "ChangeAll":
        replacement = command.split(":|:")[2]
        message = message.replace(substr, replacement)
        print(message)

    command = input()

print(f"You have a new text message: {message}")