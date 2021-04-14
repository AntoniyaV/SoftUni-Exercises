def add_elements(pos, new_numbers, numbers):
    if pos == "beginning":
        return new_numbers + numbers
    elif pos == "end":
        return numbers + new_numbers


def remove_elements(position, count, numbers):
    indices = {"beginning": 0, "end": -1}
    index = indices[position]

    if not count:
        numbers.pop(index)
        return numbers

    for _ in range(count[0]):
        numbers.pop(index)
    return numbers


def list_manipulator(numbers, *args):
    command, position, rest = args[0], args[1], list(args[2:])
    if command == "add":
        numbers = add_elements(position, rest, numbers)
    elif command == "remove":
        numbers = remove_elements(position, rest, numbers)
    return numbers


# Test code:
print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
