import re

participants_list = input().split(", ")
participants = {}

for person in participants_list:
    participants[person] = 0

info = input()

while not info == "end of race":
    name = re.findall(r"[A-Za-z]", info)
    name = "".join(name)

    if name in participants:
        distance = re.findall(r"\d", info)
        distance = sum([int(n) for n in distance])
        participants[name] += distance

    info = input()

sorted_participants = sorted(participants.items(), key=lambda x: -x[1])

print(f"1st place: {sorted_participants[0][0]}")
print(f"2nd place: {sorted_participants[1][0]}")
print(f"3rd place: {sorted_participants[2][0]}")