usernames = input().split(", ")
valid_usernames = []

for user in usernames:
    wrong_symbol = False
    if len(user) not in range(3, 17):
        continue

    for symbol in user:
        if not symbol.isdigit() and not symbol.isalpha() and not symbol == "-" and not symbol == "_":
            wrong_symbol = True
            break

    if wrong_symbol:
        continue

    valid_usernames.append(user)

for valid_user in valid_usernames:
    print(valid_user)
