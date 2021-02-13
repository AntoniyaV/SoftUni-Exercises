def find_odd_numbers(numbers):
    return list(filter(lambda x: not x % 2 == 0, numbers))


def find_even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))


def get_result(numbers, n):
    return sum(numbers) * n


command = input()
nums = [int(x) for x in input().split()]

if command == "Odd":
    print(get_result(find_odd_numbers(nums), len(nums)))
else:
    print(get_result(find_even_numbers(nums), len(nums)))