n = int(input())
matrix = []

for _ in range(n):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

new_matrix = [[num for num in r if num % 2 == 0] for r in matrix]
print(new_matrix)