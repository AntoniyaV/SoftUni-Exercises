def is_valid(n, coordinate):
    return coordinate in range(n)


def modify_matrix(some_matrix, act, r, c, val):
    if act == "Add":
        some_matrix[r][c] += val
    elif act == 'Subtract':
        some_matrix[r][c] -= val
    return some_matrix


def print_result(result):
    return [print(' '.join([str(n) for n in r])) for r in result]


num = int(input())
matrix = []

for _ in range(num):
    matrix_row = [int(x) for x in input().split()]
    matrix.append(matrix_row)

while True:
    command = input()
    if command == 'END':
        print_result(matrix)
        break

    action = command.split()[0]
    row, col, value = [int(x) for x in command.split()[1:]]

    if not is_valid(num, row) or not is_valid(len(matrix[0]), col):
        print("Invalid coordinates")
        continue

    matrix = modify_matrix(matrix, action, row, col, value)
