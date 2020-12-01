command = input()
users = {}

while not command == "Lumpawaroo":
    if "|" in command:
        side, user = command.split(" | ")
        user_exists = False

        for force_side, people in users.items():
            for person in people:
                if person == user:
                    user_exists = True

        if not user_exists:
            if side not in users:
                users[side] = [user]
            else:
                users[side].append(user)

    elif " -> " in command:
        user, side = command.split(" -> ")

        for force_side, people in users.items():
            for person in people:
                if person == user:
                    users[force_side].remove(user)
        if side not in users:
            users[side] = [user]
        else:
            users[side].append(user)

        print(f"{user} joins the {side} side!")

    command = input()

sorted_users = dict(sorted(users.items(), key=lambda x: (-len(x[1]), x[0])))

for f_side, f_users in sorted_users.items():
    if not f_users:
        continue

    f_users.sort()
    print(f"Side: {f_side}, Members: {len(f_users)}")
    for f_user in f_users:
        print(f"! {f_user}")
