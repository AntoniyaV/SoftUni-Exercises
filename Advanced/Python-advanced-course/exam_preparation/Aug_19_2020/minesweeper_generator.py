import re


def is_value_in_range(value, board_range):
    return value in range(board_range)


def calculate_count(r_i, c_i, board):
    count = 0
    board_range = len(board)

    left_i = c_i - 1
    right_i = c_i + 1
    up_i = r_i - 1
    down_i = r_i + 1

    if is_value_in_range(left_i, board_range):
        if board[r_i][left_i] == "*":
            count += 1

    if is_value_in_range(right_i, board_range):
        if board[r_i][right_i] == "*":
            count += 1

    if is_value_in_range(up_i, board_range):
        if board[up_i][c_i] == "*":
            count += 1

    if is_value_in_range(down_i, board_range):
        if board[down_i][c_i] == "*":
            count += 1

    if is_value_in_range(left_i, board_range) and is_value_in_range(up_i, board_range):
        if board[up_i][left_i] == "*":
            count += 1

    if is_value_in_range(right_i, board_range) and is_value_in_range(up_i, board_range):
        if board[up_i][right_i] == "*":
            count += 1

    if is_value_in_range(left_i, board_range) and is_value_in_range(down_i, board_range):
        if board[down_i][left_i] == "*":
            count += 1

    if is_value_in_range(right_i, board_range) and is_value_in_range(down_i, board_range):
        if board[down_i][right_i] == "*":
            count += 1

    return count


def generate_numbers_in_matrix(num, board):
    for r_i in range(num):
        for c_i in range(num):
            if not board[r_i][c_i] == "*":
                count = calculate_count(r_i, c_i, board)
                board[r_i][c_i] = count
    return board


def get_matrix_result_as_str(board):
    return '\n'.join([' '.join([str(x) for x in row]) for row in board])


n = int(input())
k = int(input())

matrix = [[0 for c in range(n)] for r in range(n)]

for _ in range(k):
    position = [int(x) for x in re.findall(f'\d+', input())]
    row_index, col_index = position
    matrix[row_index][col_index] = "*"

matrix = generate_numbers_in_matrix(n, matrix)
print(get_matrix_result_as_str(matrix))
