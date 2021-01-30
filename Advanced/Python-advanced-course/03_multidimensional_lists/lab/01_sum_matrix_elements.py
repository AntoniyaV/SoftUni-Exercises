rows, cols = [int(n) for n in input().split(', ')]
matrix = []
matrix_sum = 0

for r in range(rows):
    column = [int(x) for x in input().split(', ')]
    matrix.append(column)
    matrix_sum += sum(matrix[r])

print(matrix_sum)
print(matrix)