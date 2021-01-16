collection = input().split()
command = input()

while not command == "Stop":
    if "Delete" in command:
        index = int(command.split()[1]) + 1
        if index in range(len(collection)):
            collection.pop(index)

    elif "Swap" in command:
        word_1, word_2 = command.split()[1], command.split()[2]
        if word_1 in collection and word_2 in collection:
            index_1 = collection.index(word_1)
            index_2 = collection.index(word_2)
            collection[index_1], collection[index_2] = word_2, word_1

    elif "Put" in command:
        word, index = command.split()[1], int(command.split()[2]) - 1
        if index in range(len(collection)):
            collection.insert(index, word)
        elif index == len(collection):
            collection.append(word)

    elif "Sort" in command:
        collection.sort(reverse=True)

    elif "Replace" in command:
        word_1, word_2 = command.split()[1], command.split()[2]
        if word_2 in collection:
            index_2 = collection.index(word_2)
            collection[index_2] = word_1

    command = input()

print(' '.join(collection))