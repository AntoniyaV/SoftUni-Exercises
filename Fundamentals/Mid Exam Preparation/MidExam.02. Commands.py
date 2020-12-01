collection = input().split()
command = input()

while not command == "end":
    if "remove" in command:
        count = int(command.split()[1])
        del collection[:count]

    else:
        action, index, count = command.split()[0], int(command.split()[2]), int(command.split()[4])

        if action == "reverse":
            subcollection = [collection[i] for i in range(index, index + count)]
            subcollection.reverse()
            collection = collection[:index] + subcollection + collection[index + count:]

        elif action == "sort":
            subcollection = [collection[i] for i in range(index, index + count)]
            subcollection.sort()
            collection = collection[:index] + subcollection + collection[index + count:]

    command = input()

print(', '.join(collection))
