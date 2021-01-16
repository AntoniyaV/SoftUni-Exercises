n_rooms = int(input())

free_chairs = 0
more_people = False

for room in range(1, n_rooms + 1):
    chairs_in_room = input()
    num_chairs, taken_chairs = chairs_in_room.split()
    taken_chairs = int(taken_chairs)

    if len(num_chairs) > taken_chairs:
        free_chairs += len(num_chairs) - taken_chairs

    elif len(num_chairs) < taken_chairs:
        print(f"{taken_chairs - len(num_chairs)} more chairs needed in room {room}")
        more_people = True

if not more_people:
    print(f"Game On, {free_chairs} free chairs left")