contests = {}
info = input()

while not info == "end of contests":
    cntst, pswd = info.split(":")
    contests[cntst] = pswd

    info = input()

users = {}
user_info = input()

while not user_info == "end of submissions":
    contest, password, username, points = user_info.split("=>")
    points = int(points)

    if contest in contests and contests[contest] == password:
        if username not in users:
            users[username] = {}

        if contest not in users[username] or users[username][contest] <= points:
            users[username][contest] = points

    user_info = input()

total_points = {}
for usr, usr_contests in users.items():
    for contest_name, contest_point in usr_contests.items():

        if usr not in total_points:
            total_points[usr] = 0

        total_points[usr] += contest_point

best_user = max(total_points, key=lambda x: total_points[x])

print(f"Best candidate is {best_user} with total {total_points[best_user]} points.")
print("Ranking:")

sorted_users = dict(sorted(users.items(), key=lambda x: x[0]))
for user, user_contests in sorted_users.items():
    print(user)

    sorted_contests = dict(sorted(user_contests.items(), key=lambda x: -x[1]))
    for user_contest, contest_points in sorted_contests.items():
        print(f"#  {user_contest} -> {contest_points}")
