def check_index(some_index, some_list):
    return True if some_index in range(len(some_list)) else False


def shoot_target(some_index, some_value, some_list):
    if check_index(some_index, some_list):
        some_list[some_index] -= some_value
        if some_list[some_index] <= 0:
            some_list.pop(some_index)
    return some_list


def add_target(some_index, some_value, some_list):
    if check_index(some_index, some_list):
        some_list.insert(some_index, some_value)
    else:
        print("Invalid placement!")
    return some_list


def strike(some_index, some_value, some_list):
    start = some_index - some_value
    end = some_index + some_value
    if check_index(start, some_list) and check_index(end, some_list):
        del targets[start:end + 1]
    else:
        print("Strike missed!")
    return some_list


targets = [int(n) for n in input().split()]
command = input()

while not command == "End":
    action, index, value = command.split()
    index = int(index)
    value = int(value)

    if action == "Shoot":
        targets = shoot_target(index, value, targets)
    elif action == "Add":
        targets = add_target(index, value, targets)
    elif action == "Strike":
        targets = strike(index, value, targets)

    command = input()

print('|'.join([str(t) for t in targets]))