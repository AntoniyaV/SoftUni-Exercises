def get_missing_number(min_value, max_value, numbers):
    for number in range(min_value, max_value):
        if number not in numbers:
            return number


def get_duplicates(numbers):
    duplicates = set([num for num in numbers if numbers.count(num) > 1])
    return sorted(duplicates)


def numbers_searching(*numbers):
    min_num = min(numbers)
    max_num = max(numbers)
    missing_number = get_missing_number(min_num, max_num, numbers)
    duplicate_numbers = get_duplicates(numbers)
    return [missing_number, duplicate_numbers]


# Test code:
print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))