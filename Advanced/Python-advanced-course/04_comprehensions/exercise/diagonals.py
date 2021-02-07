def get_primary_diagonal(some_matrix):
    primary_diagonal = []
    for row_index in range(len(some_matrix)):
        primary_diagonal.append(some_matrix[row_index][row_index])
    return primary_diagonal


def get_secondary_diagonal(some_matrix):
    secondary_diagonal = []
    for row_index in range(len(some_matrix)):
        col_index = len(some_matrix) - row_index - 1
        secondary_diagonal.append(some_matrix[row_index][col_index])
    return secondary_diagonal


def print_result(some_matrix):
    first_diagonal = get_primary_diagonal(some_matrix)
    second_diagonal = get_secondary_diagonal(some_matrix)
    print(f"First diagonal: {', '.join([str(x) for x in first_diagonal])}. Sum: {sum(first_diagonal)}")
    print(f"Second diagonal: {', '.join([str(x) for x in second_diagonal])}. Sum: {sum(second_diagonal)}")


n = int(input())
matrix = []

for _ in range(n):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

print_result(matrix)
