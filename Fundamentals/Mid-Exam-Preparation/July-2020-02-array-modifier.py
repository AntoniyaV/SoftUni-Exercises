numbers = [int(n) for n in input().split()]
command = input()

while not command == "end":
    if command == "decrease":
        numbers = [n - 1 for n in numbers]
    else:
        index_1 = int(command.split()[1])
        index_2 = int(command.split()[2])

        if "swap" in command:
            numbers[index_1], numbers[index_2] = numbers[index_2], numbers[index_1]

        elif "multiply" in command:
            numbers[index_1] *= numbers[index_2]

    command = input()

print(', '.join([str(n) for n in numbers]))