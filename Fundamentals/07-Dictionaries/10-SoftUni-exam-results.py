command = input()
users = {}
languages = {}

while not command == "exam finished":
    username = command.split("-")[0]
    if "banned" in command:
        users.pop(username)
        command = input()
        continue

    language = command.split("-")[1]
    points = int(command.split("-")[2])

    if username not in users:
        users[username] = points

    else:
        if users[username] < points:
            users[username] = points

    if language not in languages:
        languages[language] = [username]
    else:
        languages[language].append(username)

    command = input()

sorted_users = dict(sorted(users.items(), key=lambda x: (-x[1], x[0])))
print("Results:")

for user, grade in sorted_users.items():
    print(f"{user} | {grade}")

sorted_languages = dict(sorted(languages.items(), key=lambda x:(-len(x[1]), x[0])))
print("Submissions:")

for technology, submissions in sorted_languages.items():
    print(f"{technology} - {len(submissions)}")
