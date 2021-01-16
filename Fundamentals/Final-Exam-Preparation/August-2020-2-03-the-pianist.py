num = int(input())

pieces = {}

for n in range(num):
    piece, composer, key = input().split("|")
    pieces[piece] = [composer, key]


def piece_is_present(some_piece, some_collection):
    return True if some_piece in some_collection else False


command = input()

while not command == "Stop":
    action, name = command.split("|")[0], command.split("|")[1]

    if action == "Add":
        if piece_is_present(name, pieces):
            print(f"{name} is already in the collection!")
        else:
            some_composer, some_key = command.split("|")[2], command.split("|")[3]
            pieces[name] = [some_composer, some_key]

            print(f"{name} by {some_composer} in {some_key} added to the collection!")

    elif action == "Remove":
        if piece_is_present(name, pieces):
            pieces.pop(name)
            print(f"Successfully removed {name}!")
        else:
            print(f"Invalid operation! {name} does not exist in the collection.")

    elif action == "ChangeKey":
        if piece_is_present(name, pieces):
            new_key = command.split("|")[2]
            pieces[name][1] = new_key
            print(f"Changed the key of {name} to {new_key}!")
        else:
            print(f"Invalid operation! {name} does not exist in the collection.")

    command = input()

sorted_pieces = dict(sorted(pieces.items(), key=lambda x: (x[0], x[1][0])))

for sorted_piece, values in sorted_pieces.items():
    print(f"{sorted_piece} -> Composer: {values[0]}, Key: {values[1]}")