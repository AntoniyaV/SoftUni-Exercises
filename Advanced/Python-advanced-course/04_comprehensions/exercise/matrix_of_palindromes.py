def create_palindrome_matrix(row, col, alphabet):
    matrix = []
    for r_i in range(row):
        matrix.append([])
        for c_i in range(col):
            current_palindrome = alphabet[r_i] + alphabet[r_i + c_i] + alphabet[r_i]
            matrix[r_i].append(current_palindrome)
    return matrix


def print_result(result):
    return [print(' '.join(row)) for row in result]


r, c = [int(x) for x in input().split()]
letters = 'abcdefghijklmnopqrstuvwxyz'
palindrome_matrix = create_palindrome_matrix(r, c, letters)
print_result(palindrome_matrix)
