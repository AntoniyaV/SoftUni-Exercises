password = input()
command = input()

while not command == "Done":
    if command == "TakeOdd":
        password_holder = ''

        for i in range(len(password)):
            if not i % 2 == 0:
                password_holder += password[i]

        password = password_holder
        print(password)

    elif "Cut" in command:
        index, length = int(command.split()[1]), int(command.split()[2])
        password = password[:index] + password[index + length:]
        print(password)

    elif "Substitute" in command:
        substring, substitute = command.split()[1], command.split()[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {password}")
