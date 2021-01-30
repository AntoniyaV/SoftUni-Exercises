from collections import deque


def track_snake_path(m_rows, m_cols, snake_sequence):
    some_matrix = []
    for r in range(m_rows):
        some_matrix.append([])
        for c in range(m_cols):
            some_matrix[r].append(snake_sequence[0])
            snake_sequence.append(snake_sequence.popleft())
    return some_matrix


def print_result(result):
    for row_index in range(len(result)):
        if not row_index % 2 == 0:
            result[row_index] = result[row_index][::-1]
        print(''.join(result[row_index]))


rows, cols = [int(x) for x in input().split()]
snake = deque(input())

matrix = track_snake_path(rows, cols, snake)
print_result(matrix)
