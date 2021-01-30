def find_primary_diagonal_sum(some_matrix):
    diagonal_sum = 0
    row_length = len(some_matrix)
    col_length = len(some_matrix[0])

    for r in range(row_length):
        for c in range(col_length):
            if r == c:
                diagonal_sum += matrix[r][c]

    return diagonal_sum


n = int(input())
matrix = []

for _ in range(n):
    column = [int(x) for x in input().split()]
    matrix.append(column)

primary_diagonal_sum = find_primary_diagonal_sum(matrix)
print(primary_diagonal_sum)
