from collections import deque

duration_green_light = int(input())
duration_free_window = int(input())
total_cars_passed = 0
cars = deque()

while True:
    command = input()
    everyone_is_safe = False
    there_is_a_crush = False

    if command == 'END':
        everyone_is_safe = True
        break

    if command == 'green':
        green_light = duration_green_light
        free_window = duration_free_window

        for _ in range(len(cars)):
            if green_light == 0:
                continue

            if len(cars[0]) <= green_light:
                green_light -= len(cars[0])
                cars.popleft()
                total_cars_passed += 1

            elif len(cars[0]) <= green_light + free_window:
                free_window -= len(cars[0]) - green_light
                green_light = 0
                cars.popleft()
                total_cars_passed += 1

            else:
                crush_index = green_light + free_window
                print('A crash happened!')
                print(f'{cars[0]} was hit at {cars[0][crush_index]}.')
                there_is_a_crush = True
                break

    else:
        cars.append(command)

    if there_is_a_crush:
        break

if everyone_is_safe:
    print('Everyone is safe.')
    print(f'{total_cars_passed} total cars passed the crossroads.')