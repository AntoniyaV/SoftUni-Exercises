from collections import deque


def print_cups(cups):
    print(f"Cups: {' '.join([str(cups.popleft()) for _ in range(len(cups))])}")


def print_bottles(bottles):
    print(f"Bottles: {' '.join([str(bottles.pop()) for _ in range(len(bottles))])}")


cups_capacities = deque([int(x) for x in input().split()])
filled_bottles = [int(x) for x in input().split()]
wasted_water = 0

while True:
    if not cups_capacities:
        print_bottles(filled_bottles)
        break

    if not filled_bottles:
        print_cups(cups_capacities)
        break

    current_bottle = filled_bottles.pop()

    if cups_capacities[0] <= current_bottle:
        wasted_water += current_bottle - cups_capacities[0]
        cups_capacities.popleft()

    else:
        cups_capacities[0] -= current_bottle

print(f"Wasted litters of water: {wasted_water}")