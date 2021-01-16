targets = [int(n) for n in input().split()]
index = input()

shot_targets = 0

while not index == "End":
    index = int(index)

    if index not in range(len(targets)):
        index = input()
        continue

    if not targets[index] == -1:
        current_target = targets[index]
        targets[index] = -1
        shot_targets += 1

        for i in range(len(targets)):
            if targets[i] == -1:
                continue

            if targets[i] > current_target:
                targets[i] -= current_target
            else:
                targets[i] += current_target

    index = input()

print(f"Shot targets: {shot_targets} -> {' '.join([str(t) for t in targets])}")