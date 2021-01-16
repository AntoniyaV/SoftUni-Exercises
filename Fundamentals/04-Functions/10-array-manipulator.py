def exchange_elements(index, list_of_ints):
    if index < 0 or index > len(list_of_ints) - 1:
        return "Invalid index"

    list_holder = list_of_ints[index + 1:] + list_of_ints[:index + 1]
    return list_holder


def max_even_or_odd_indx(some_command, list_of_ints):
    max_num = -9999999999

    if "even" in some_command:
        for num in list_of_ints:
            if num % 2 == 0 and num > max_num:
                max_num = num

    elif "odd" in some_command:
        for num in list_of_ints:
            if not num % 2 == 0 and num > max_num:
                max_num = num

    if not max_num == -9999999999:
        max_num_index = len(list_of_ints)
        for el in range(len(list_of_ints) - 1, -1, -1):
            max_num_index -= 1
            if list_of_ints[el] == max_num:
                return max_num_index
    else:
        return "No matches"


def min_even_or_odd_indx(some_command, list_of_ints):
    min_num = 9999999999

    if "even" in some_command:
        for num in list_of_ints:
            if num % 2 == 0 and num < min_num:
                min_num = num

    elif "odd" in some_command:
        for num in list_of_ints:
            if not num % 2 == 0 and num < min_num:
                min_num = num

    if not min_num == 9999999999:
        min_num_index = len(list_of_ints)
        for el in range(len(list_of_ints) - 1, -1, -1):
            min_num_index -= 1
            if list_of_ints[el] == min_num:
                return min_num_index
    else:
        return "No matches"


def first_even_or_odd_count(some_command, list_of_ints):
    if int(some_command[1]) > len(list_of_ints):
        return "Invalid count"

    first_even_or_odd = []
    if "even" in some_command:
        for n in list_of_ints:
            if len(first_even_or_odd) == int(some_command[1]):
                break
            if n % 2 == 0:
                first_even_or_odd.append(n)

    elif "odd" in some_command:
        for n in list_of_ints:
            if len(first_even_or_odd) == int(some_command[1]):
                break
            if not n % 2 == 0:
                first_even_or_odd.append(n)

    return first_even_or_odd


def last_even_or_odd_count(some_command, list_of_ints):
    if int(some_command[1]) > len(list_of_ints):
        return "Invalid count"

    last_even_or_odd = []
    if "even" in some_command:
        for n in range(len(list_of_ints) - 1, -1, -1):
            if len(last_even_or_odd) == int(some_command[1]):
                break
            if list_of_ints[n] % 2 == 0:
                last_even_or_odd.append(list_of_ints[n])

    elif "odd" in some_command:
        for n in range(len(list_of_ints) - 1, -1, -1):
            if len(last_even_or_odd) == int(some_command[1]):
                break
            if not list_of_ints[n] % 2 == 0:
                last_even_or_odd.append(list_of_ints[n])

    last_even_or_odd.reverse()
    return last_even_or_odd


integers = input().split()
integers = [int(i) for i in integers]
command = input()

while not command == "end":
    if "exchange" in command:
        command_name, command_index = command.split()
        command_index = int(command_index)
        result = exchange_elements(command_index, integers)
        if type(result) == str:
            print(result)
        else:
            integers = result

    elif "max" in command:
        print(max_even_or_odd_indx(command, integers))

    elif "min" in command:
        print(min_even_or_odd_indx(command, integers))

    elif "first" in command:
        command = command.split()
        print(first_even_or_odd_count(command, integers))

    elif "last" in command:
        command = command.split()
        print(last_even_or_odd_count(command, integers))

    command = input()

print(integers)
