def is_valid(number):
    division_range = range(2, 11)
    return any([number % x == 0 for x in division_range])


def get_valid_numbers(some_numbers):
    return [n for n in some_numbers if is_valid(n)]


start = int(input())
end = int(input())
numbers = [num for num in range(start, end + 1)]

result = get_valid_numbers(numbers)
print(result)