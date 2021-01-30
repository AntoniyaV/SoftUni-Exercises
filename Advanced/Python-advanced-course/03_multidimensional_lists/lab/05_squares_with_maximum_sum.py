def calculate_submatrix_sum(row_index, col_index, some_matrix, square_size=2):
    submatrix_sum = 0

    for r in range(row_index, row_index + square_size):
        for c in range(col_index, col_index + square_size):
            submatrix_sum += some_matrix[r][c]

    return submatrix_sum


def find_square_with_max_sum_coordinates(n_rows, n_cols, some_matrix):
    max_sum = 0
    max_row = 0
    max_col = 0

    for r_index in range(n_rows - 1):
        for c_index in range(n_cols - 1):
            current_sum = calculate_submatrix_sum(r_index, c_index, some_matrix)
            if current_sum > max_sum:
                max_sum = current_sum
                max_row = r_index
                max_col = c_index

    return max_row, max_col


def get_square_with_max_sum(sq_coordinates, some_matrix, square_size=2):
    index_row, index_col = sq_coordinates
    square = []
    sq_i = 0

    for r_i in range(index_row, index_row + square_size):
        square.append([])
        for c_i in range(index_col, index_col + square_size):
            square[sq_i].append(some_matrix[r_i][c_i])
        sq_i += 1

    return square


def print_result(found_square):
    sq_sum = 0
    for row in found_square:
        print(' '.join([str(n) for n in row]))
        sq_sum += sum(row)

    print(sq_sum)


rows, cols = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows):
    column = [int(x) for x in input().split(', ')]
    matrix.append(column)

max_sum_square_info = find_square_with_max_sum_coordinates(rows, cols, matrix)
max_sum_square = get_square_with_max_sum(max_sum_square_info, matrix)
print_result(max_sum_square)
