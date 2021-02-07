def create_matrix_from_input(some_input):
    return [[int(x) for x in nums.split()] for nums in some_input.split('|') ]


def reverse_and_flatten_matrix(some_matrix):
    return [x for row in some_matrix[::-1] for x in row]


matrix = create_matrix_from_input(input())
flattened_matrix = reverse_and_flatten_matrix(matrix)
print(' '.join([str(n) for n in flattened_matrix]))
