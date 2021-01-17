from collections import deque

num_pumps = int(input())
pumps = deque()

for n in range(num_pumps):
    pumps.append([int(x) for x in input().split()])

for i in range(num_pumps):
    total_amount = 0
    is_complete = True

    for pump in pumps:
        amount = pump[0]
        distance = pump[1]
        total_amount += amount

        if total_amount < distance:
            pumps.append(pumps.popleft())
            is_complete = False
            break

        total_amount -= distance

    if is_complete:
        print(i)
        break
