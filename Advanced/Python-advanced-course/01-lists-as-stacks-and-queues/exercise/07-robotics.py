from collections import deque


def robot_working_time(robots_input):
    robot_dict = {}

    for pair in robots_input:
        robot_name, process_time = pair.split('-')
        robot_dict[robot_name] = int(process_time)

    return robot_dict


def transform_time_to_seconds(input_time):
    hs, ms, ss = input_time.split(':')
    return int(hs) * 3600 + int(ms) * 60 + int(ss)


def robot_starting_time(info, time):
    return {name: time + 1 for name in info}


def format_time(time):
    time = time % (24 * 3600)
    hours = time // 3600
    minutes = (time % 3600) // 60
    seconds = time % 60
    return "%02d:%02d:%02d" % (hours, minutes, seconds)


robots_info = robot_working_time(input().split(';'))
starting_time = transform_time_to_seconds(input())
robots = robot_starting_time(robots_info, starting_time)

products = deque()

while True:
    command = input()

    if command == 'End':
        break

    products.append(command)

while products:
    starting_time += 1
    is_processed = False

    for robot in robots:
        if robots[robot] <= starting_time:
            print(f'{robot} - {products.popleft()} [{format_time(starting_time)}]')
            robots[robot] = starting_time + robots_info[robot]
            is_processed = True
            break

    if not is_processed:
        products.append(products.popleft())
