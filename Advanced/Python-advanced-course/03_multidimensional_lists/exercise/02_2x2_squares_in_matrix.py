def check_matrix_validity(row_index, col_index, some_matrix, character, size=2):
    for r_i in range(row_index, row_index + size):
        for c_i in range(col_index, col_index + size):
            if not some_matrix[r_i][c_i] == character:
                return False
    return True


def find_count_of_matrices_with_same_chars(matrix_rows, matrix_cols, some_matrix):
    valid_matrices_count = 0
    for r in range(matrix_rows - 1):
        for c in range(matrix_cols - 1):
            current_char = some_matrix[r][c]
            if check_matrix_validity(r, c, some_matrix, current_char):
                valid_matrices_count += 1

    return valid_matrices_count


rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    row = input().split()
    matrix.append(row)

found_matrices_count = find_count_of_matrices_with_same_chars(rows, cols, matrix)
print(found_matrices_count)
