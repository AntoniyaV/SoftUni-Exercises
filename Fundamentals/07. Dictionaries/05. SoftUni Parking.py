def register_user(user, license_plate, all_users):
    if user not in all_users:
        all_users[user] = license_plate
        print(f"{user} registered {license_plate} successfully")

    else:
        print(f"ERROR: already registered with plate number {all_users[user]}")

    return all_users


def unregister_user(user, all_users):
    if user not in all_users:
        print(f"ERROR: user {user} not found")

    else:
        print(f"{user} unregistered successfully")
        all_users.pop(user)

    return all_users


n = int(input())
users = {}

for _ in range(n):
    command = input().split()
    action = command[0]
    username = command[1]

    if action == "register":
        plate = command[2]
        users = register_user(username, plate, users)

    elif action == "unregister":
        users = unregister_user(username, users)

for key, value in users.items():
    print(f"{key} => {value}")