def command_is_valid(some_command):
    some_command = some_command.split()
    if some_command[0] == 'swap' and len(some_command) == 5:
        return True
    return False


def coordinate_is_valid(coordinates_to_check, valid_range):
    for value in coordinates_to_check:
        if value not in range(valid_range):
            return False
    return True


def swap_values_in_matrix(row1, col1, row2, col2, some_matrix):
    some_matrix[row1][col1], some_matrix[row2][col2] = some_matrix[row2][col2], some_matrix[row1][col1]
    return some_matrix


def print_result(result):
    for r in result:
        print(' '.join([str(n) for n in r]))


rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

while True:
    command = input()

    if command == 'END':
        break

    if not command_is_valid(command):
        print('Invalid input!')
        continue

    row_1, col_1, row_2, col_2 = [int(x) for x in command.split() if x.isdigit()]

    if not coordinate_is_valid([row_1, row_2], rows) or not coordinate_is_valid([col_1, col_2], cols):
        print('Invalid input!')
        continue

    matrix = swap_values_in_matrix(row_1, col_1, row_2, col_2, matrix)
    print_result(matrix)
