num_rows = int(input())

all_rows = []

for row in range(num_rows):
    current_row = input()
    all_rows.append(current_row)

attacked_squares = input().split()
destroyed_ships = 0

for square in attacked_squares:
    square_row, square_col = square.split("-")
    square_row, square_col = int(square_row), int(square_col)

    target_row = all_rows[square_row].split()
    target_row = list(map(lambda n: int(n), target_row))

    if target_row[square_col] > 0:
        target_row[square_col] -= 1
        if target_row[square_col] == 0:
            destroyed_ships += 1

    target_row = list(map(lambda x: str(x), target_row))
    str_target_row = " ".join(target_row)
    all_rows[square_row] = str_target_row

print(destroyed_ships)
