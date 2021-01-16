email = input()

command = input()

while not command == "Complete":
    if command == "Make Upper":
        email = email.upper()
        print(email)

    elif command == "Make Lower":
        email = email.lower()
        print(email)

    elif "GetDomain" in command:
        count = int(command.split()[1])
        print(email[-count:])

    elif command == "GetUsername":
        if "@" in email:
            index = email.index('@')
            print(email[:index])

        else:
            print(f"The email {email} doesn't contain the @ symbol.")

    elif "Replace" in command:
        char = command.split()[1]
        email = email.replace(char, '-')
        print(email)

    elif command == "Encrypt":
        encrypted_mail = [ord(sym) for sym in email]
        print(' '.join([str(n) for n in encrypted_mail]))

    command = input()