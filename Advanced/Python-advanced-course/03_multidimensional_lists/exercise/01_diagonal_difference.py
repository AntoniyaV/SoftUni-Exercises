def find_primary_diagonal_sum(some_matrix):
    primary_sum = 0
    for r in range(len(some_matrix)):
        primary_sum += some_matrix[r][r]

    return primary_sum


def find_secondary_diagonal_sum(some_matrix):
    secondary_sum = 0
    for r in range(len(some_matrix)):
        secondary_sum += some_matrix[r][len(some_matrix) - r - 1]

    return secondary_sum


n = int(input())
matrix = []

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

primary_diagonal_sum = find_primary_diagonal_sum(matrix)
secondary_diagonal_sum = find_secondary_diagonal_sum(matrix)

abs_difference = abs(primary_diagonal_sum - secondary_diagonal_sum)
print(abs_difference)
