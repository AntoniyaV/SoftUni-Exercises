def process_input(some_input):
    return [int(x) for x in some_input.split(', ')]


def get_positive(nums):
    return [num for num in nums if num >= 0]


def get_negative(nums):
    return [num for num in nums if num < 0]


def get_even(nums):
    return [num for num in nums if num % 2 == 0]


def get_odd(nums):
    return [num for num in nums if not num % 2 == 0]


def combine_all(nums):
    combined = {
        'Positive': get_positive(nums),
        'Negative': get_negative(nums),
        'Even': get_even(nums),
        'Odd': get_odd(nums)
    }
    return combined


def joined(nums):
    return ', '.join([str(x) for x in nums])


def print_result(result):
    return [print(f'{ns_type}: {joined(ns)}') for ns_type, ns in result.items()]


numbers = process_input(input())
all_types = combine_all(numbers)
print_result(all_types)
