def bomb_damage(value, r, c, some_matrix):
    start_row = r - 1
    size = len(some_matrix)

    for _ in range(3):
        if start_row not in range(size):
            start_row += 1
            continue

        start_col = c - 1

        for _ in range(3):
            if start_col not in range(size):
                start_col += 1
                continue

            if some_matrix[start_row][start_col] > 0:
                some_matrix[start_row][start_col] -= value
            start_col += 1

        start_row += 1

    return some_matrix


def detonate_bombs(bombs_info, some_matrix):
    for info in bombs_info:
        row_index, col_index = [int(x) for x in info.split(',')]

        if some_matrix[row_index][col_index] <= 0:
            continue

        bomb_value = some_matrix[row_index][col_index]
        some_matrix[row_index][col_index] = 0
        some_matrix = bomb_damage(bomb_value, row_index, col_index, some_matrix)

    return some_matrix


def get_alive_cells_(size, some_matrix):
    alive_cells = []
    for r in range(size):
        for c in range(size):
            if some_matrix[r][c] > 0:
                alive_cells.append(some_matrix[r][c])

    return alive_cells


def print_result(size, result):
    alive_cells = get_alive_cells_(size, result)

    print(f'Alive cells: {len(alive_cells)}')
    print(f'Sum: {sum(alive_cells)}')

    for r in result:
        print(' '.join([str(num) for num in r]))


n = int(input())
matrix = []

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

bombs_coordinates = input().split()

matrix = detonate_bombs(bombs_coordinates, matrix)
print_result(n, matrix)
