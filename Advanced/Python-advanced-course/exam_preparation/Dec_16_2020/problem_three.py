def is_index_in_range(index, indices_range):
    return index in range(indices_range)


def get_valid_index_from_two(index_1, index_2, indices_range):
    return index_1 if is_index_in_range(index_1, indices_range) else index_2


def generate_new_row(previous):
    previous_range = len(previous)
    next_row = [0 for _ in range(previous_range + 1)]

    for index in range(len(next_row)):
        if is_index_in_range(index - 1, previous_range) and is_index_in_range(index, previous_range):
            next_row[index] = previous[index - 1] + previous[index]
        else:
            valid_index = get_valid_index_from_two(index - 1, index, previous_range)
            next_row[index] = previous[valid_index]

    return next_row


def get_magic_triangle(n):
    triangle = [[1], [1, 1]]

    for i in range(2, n):
        previous_row = triangle[i-1]
        new_row = generate_new_row(previous_row)
        triangle.append(new_row)

    return triangle


# Test code:
print(get_magic_triangle(5))