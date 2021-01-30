def print_matrix_columns_sum(n_rows, n_cols, some_matrix):
    for col in range(n_cols):
        col_sum = 0
        for row in range(n_rows):
            col_sum += some_matrix[row][col]
        print(col_sum)


rows, cols = [int(x) for x in input().split(', ')]
matrix = []

for r in range(rows):
    column = [int(x) for x in input().split()]
    matrix.append(column)

print_matrix_columns_sum(rows, cols, matrix)
