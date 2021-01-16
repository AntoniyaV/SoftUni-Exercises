elements = input().split()
indexes = input()
moves = 0

while not indexes == "end":
    index_1, index_2 = indexes.split()
    index_1, index_2 = int(index_1), int(index_2)
    moves += 1

    if index_1 == index_2 \
            or index_1 < 0 or index_1 >= len(elements) \
            or index_2 < 0 or index_2 >= len(elements):
        middle = int(len(elements) / 2)
        element_to_add = f"-{moves}a"

        elements.insert(middle, element_to_add)
        elements.insert(middle, element_to_add)

        print("Invalid input! Adding additional elements to the board")

    elif elements[index_1] == elements[index_2]:
        print(f"Congrats! You have found matching elements - {elements[index_1]}!")
        if index_1 > index_2:
            elements.pop(index_1)
            elements.pop(index_2)
        else:
            elements.pop(index_2)
            elements.pop(index_1)

        if not elements:
            print(f"You have won in {moves} turns!")
            break

    elif not elements[index_1] == elements[index_2]:
        print("Try again!")

    indexes = input()

if elements:
    print("Sorry you lose :(")
    print(' '.join(elements))
