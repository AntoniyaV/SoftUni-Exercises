time = input().split()

time = [int(n) for n in time]
middle = int(len(time) / 2)

left_car = time[:middle]
right_car = time[:middle:-1]

time_left_car = 0
time_right_car = 0

for n_left in left_car:
    if n_left == 0:
        time_left_car *= 0.8
    else:
        time_left_car += n_left

for n_right in right_car:
    if n_right == 0:
        time_right_car *= 0.8
    else:
        time_right_car += n_right

if time_left_car < time_right_car:
    print(f"The winner is left with total time: {time_left_car:.1f}")

else:
    print(f"The winner is right with total time: {time_right_car:.1f}")
