def calculate_submatrix_sum(m_row, m_col, some_matrix, size=3):
    subm_sum = 0
    for subm_row in range(m_row, m_row + size):
        for subm_col in range(m_col, m_col + size):
            subm_sum += some_matrix[subm_row][subm_col]

    return subm_sum


def get_matrix_with_max_sum_info(matrix_row, matrix_col, some_matrix, size=3):
    max_sum = 0
    max_row_index = 0
    max_col_index = 0

    for r in range(matrix_row - size + 1):
        for c in range(matrix_col - size + 1):
            current_sum = calculate_submatrix_sum(r, c, some_matrix)
            if current_sum > max_sum:
                max_sum = current_sum
                max_row_index = r
                max_col_index = c

    return max_sum, max_row_index, max_col_index


def print_result(info, some_matrix, size=3):
    matrix_sum, matrix_row_i, matrix_col_i = [int(x) for x in info]
    print(f"Sum = {matrix_sum}")

    for rw in range(matrix_row_i, matrix_row_i + size):
        current_row = some_matrix[rw][matrix_col_i: matrix_col_i + size]
        print(' '.join([str(n) for n in current_row]))


rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

matrix_with_max_sum_info = get_matrix_with_max_sum_info(rows, cols, matrix)
print_result(matrix_with_max_sum_info, matrix)
