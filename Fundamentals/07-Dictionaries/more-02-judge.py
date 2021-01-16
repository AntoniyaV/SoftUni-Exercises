contests = {}
contestants = {}

info = input()

while not info == "no more time":
    username, contest, points = info.split(" -> ")
    points = int(points)

    if contest not in contests:
        contests[contest] = {}

    if username not in contests[contest] or contests[contest][username] <= points:
        contests[contest][username] = points

    if username not in contestants:
        contestants[username] = 0

    info = input()

for contest_name, users in contests.items():
    print(f"{contest_name}: {len(users)} participants")

    sorted_users = dict(sorted(users.items(), key=lambda x: (-x[1], x[0])))
    n = 0

    for user, user_points in sorted_users.items():
        n += 1
        print(f"{n}. {user} <::> {user_points}")

        contestants[user] += sorted_users[user]

sorted_contestants = dict(sorted(contestants.items(), key=lambda x: (-x[1], x[0])))

print("Individual standings:")
position = 0

for contestant, total_points in sorted_contestants.items():
    position += 1
    print(f"{position}. {contestant} -> {total_points}")
