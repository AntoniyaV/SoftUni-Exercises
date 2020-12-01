energy = int(input())
distance = input()
won_battles = 0
has_failed = False

while not distance == "End of battle":
    distance = int(distance)

    if energy < distance:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
        has_failed = True
        break
    else:
        energy -= distance
        won_battles += 1
        if won_battles % 3 == 0:
            energy += won_battles

    distance = input()

if not has_failed:
    print(f"Won battles: {won_battles}. Energy left: {energy}")