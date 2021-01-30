def find_symbol_in_matrix(some_symbol, some_matrix):
    length = len(matrix)

    for r in range(length):
        for c in range(length):
            if some_matrix[r][c] == some_symbol:
                return [r, c]


def print_result(result, some_symbol):
    if result:
        print(tuple(result))
    else:
        print(f'{some_symbol} does not occur in the matrix')


n = int(input())
matrix = []

for row_i in range(n):
    col_input = input()
    matrix.append([])
    for col_i in range(n):
        matrix[row_i].append(col_input[col_i])

symbol = input()
symbol_position = find_symbol_in_matrix(symbol, matrix)
print_result(symbol_position, symbol)

