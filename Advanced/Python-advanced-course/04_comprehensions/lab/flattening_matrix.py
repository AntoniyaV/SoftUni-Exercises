def flatten_matrix(some_matrix):
    return [x for r in some_matrix for x in r]


n = int(input())
matrix = []

for _ in range(n):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

print(flatten_matrix(matrix))
