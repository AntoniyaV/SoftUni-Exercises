n = int(input())

opening = 0
closing = 0
two_consec = ""
old_command = ''

for i in range(1, n + 1):
    command = input()

    if command == "(":
        opening += 1
        if command == old_command:
            two_consec = "yes"
    elif command == ")":
        closing += 1

    if command == "(" or command == ")":
        old_command = command

if opening == closing and two_consec == "":
    print("BALANCED")
else:
    print("UNBALANCED")