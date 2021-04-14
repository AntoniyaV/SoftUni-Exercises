def get_player_position(num, board, symbol):
    for r_index in range(num):
        for c_index in range(num):
            if board[r_index][c_index] == symbol:
                return r_index, c_index


def get_new_position(row, col, direction):
    directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
    new_row = row + directions[direction][0]
    new_col = col + directions[direction][1]
    return new_row, new_col


def is_position_in_range(index_1, index_2, indices_range):
    return index_1 in range(indices_range) and index_2 in range(indices_range)


def get_matrix_info_as_str(board):
    return '\n'.join([''.join(row) for row in board])


text = input()
n = int(input())

matrix = []
for _ in range(n):
    matrix.append(list(input()))

PLAYER_SYMBOL = "P"
EMPTY_SYMBOL = "-"
current_row, current_col = get_player_position(n, matrix, PLAYER_SYMBOL)

m = int(input())
for _ in range(m):
    command = input()
    next_row, next_col = get_new_position(current_row, current_col, command)

    if not is_position_in_range(next_row, next_col, n):
        text = text[:-1]
        continue

    if not matrix[next_row][next_col] == EMPTY_SYMBOL:
        text += matrix[next_row][next_col]

    matrix[current_row][current_col] = EMPTY_SYMBOL
    matrix[next_row][next_col] = PLAYER_SYMBOL
    current_row, current_col = next_row, next_col


print(text)
print(get_matrix_info_as_str(matrix))
