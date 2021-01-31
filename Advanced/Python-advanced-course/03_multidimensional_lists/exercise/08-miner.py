def get_start_coordinates(matrix):
    for r in range(len(matrix)):
        if 's' in matrix[r]:
            return [r, matrix[r].index('s')]


def get_current_position(command, r, c):
    if command == 'up':
        r -= 1
    elif command == 'down':
        r += 1
    elif command == 'left':
        c -= 1
    elif command == 'right':
        c += 1
    return [r, c]


def get_total_coal_in_field(matrix):
    coal_count = 0
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == 'c':
                coal_count += 1
    return coal_count


def result_of_miner_movements(movements, matrix):
    r, c = get_start_coordinates(matrix)
    coal = get_total_coal_in_field(matrix)

    for command in movements:
        current_row, current_col = get_current_position(command, r, c)
        if current_row not in range(len(matrix)) or current_col not in range(len(matrix)):
            continue

        if matrix[current_row][current_col] == 'c':
            coal -= 1
            matrix[current_row][current_col] = '*'
            if coal == 0:
                return f"You collected all coals! ({current_row}, {current_col})"

        elif matrix[current_row][current_col] == 'e':
            return f"Game over! ({current_row}, {current_col})"

        r = current_row
        c = current_col

    return f"{coal} coals left. ({r}, {c})"


n = int(input())
commands = input().split()
field = []

for _ in range(n):
    row = input().split()
    field.append(row)

game_result = result_of_miner_movements(commands, field)
print(game_result)
