steps_inpt = input()
total_steps = 0

while steps_inpt != "Going home":
    steps = int(steps_inpt)
    total_steps += steps
    if total_steps >= 10000:
        break
    steps_inpt = input()

if total_steps < 10000:
    steps_inpt = int(input())
    total_steps += steps_inpt

if total_steps < 10000:
    print(f"{10000 - total_steps} more steps to reach goal.")
else:
    print("Goal reached! Good job!")
    print(f"{total_steps - 10000} steps over the goal!")