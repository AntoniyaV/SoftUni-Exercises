def generate_matrix(num):
    mtrx = []
    for _ in range(num):
        mtrx.append(list(input()))
    return mtrx


def get_element_position(num, board, symbol):
    position = []
    for row_index in range(num):
        for col_index in range(num):
            if board[row_index][col_index] == symbol:
                position.append([row_index, col_index])
    return position


def get_next_position(current_row, current_col, direction):
    directions = {"left": [0, -1], "right": [0, 1], "up": [-1, 0], "down": [1, 0]}
    value = directions[direction]
    new_row = current_row + value[0]
    new_col = current_col + value[1]
    return new_row, new_col


def is_in_range(val, num):
    return val in range(num)


def get_game_result(snake_is_fed):
    if snake_is_fed:
        return "You won! You fed the snake."
    return "Game over!"


def get_matrix_for_print(board):
    return '\n'.join([''.join(row) for row in board])


n = int(input())
matrix = generate_matrix(n)

snake_symbol = "S"
burrow_symbol = "B"
food_symbol = "*"
trail_symbol = "."

row_i, col_i = get_element_position(n, matrix, snake_symbol)[0]
burrow_position = get_element_position(n, matrix, burrow_symbol)

food = 0
is_fed = False

while True:
    command = input()
    matrix[row_i][col_i] = trail_symbol
    next_row_i, next_col_i = get_next_position(row_i, col_i, command)

    if not is_in_range(next_row_i, n) or not is_in_range(next_col_i, n):
        break

    if matrix[next_row_i][next_col_i] == food_symbol:
        food += 1

    elif matrix[next_row_i][next_col_i] == burrow_symbol:
        matrix[next_row_i][next_col_i] = trail_symbol
        burrow_position.remove([next_row_i, next_col_i])
        next_row_i, next_col_i = burrow_position[0]

    row_i, col_i = next_row_i, next_col_i
    matrix[row_i][col_i] = snake_symbol
    if food == 10:
        is_fed = True
        break


print(get_game_result(is_fed))
print(f"Food eaten: {food}")
print(get_matrix_for_print(matrix))
