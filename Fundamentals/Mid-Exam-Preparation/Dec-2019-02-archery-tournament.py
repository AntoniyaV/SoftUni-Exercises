targets = input().split("|")
targets = [int(n) for n in targets]
command = input()

points = 0

while not command == "Game over":
    if "Shoot" in command:
        start_index = int(command.split("@")[1])
        length = int(command.split("@")[2])

        if 0 <= start_index < len(targets):
            position = 0
            if "Left" in command:
                position = start_index - length

            elif "Right" in command:
                position = start_index + length

            if abs(position) >= len(targets):
                position = position % len(targets)

            if targets[position] < 5:
                points += targets[position]
                targets[position] = 0
            else:
                points += 5
                targets[position] -= 5

    elif "Reverse" in command:
        targets.reverse()

    command = input()

str_targets = [str(t) for t in targets]
print(" - ".join(str_targets))
print(f"Iskren finished the archery tournament with {points} points!")