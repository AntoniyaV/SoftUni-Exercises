from collections import deque


def is_pouch_filled(bomb_pouch):
    for bomb in bomb_pouch:
        if bomb_pouch[bomb] < 3:
            return False
    return True


def get_result_message(bomb_pouch):
    if is_pouch_filled(bomb_pouch):
        return "Bene! You have successfully filled the bomb pouch!"
    return "You don't have enough materials to fill the bomb pouch."


def get_collection_result(collection):
    res = "empty"
    if collection:
        res = ', '.join([str(x) for x in collection])
    return res


def get_bomb_pouch_result(bomb_pouch):
    return '\n'.join([f"{name}: {count}" for name, count in bomb_pouch.items()])


bomb_effects = deque([int(x) for x in input().split(",")])
bomb_casings = [int(x) for x in input().split(",")]

materials = {40: "Datura Bombs", 60: "Cherry Bombs", 120: "Smoke Decoy Bombs"}
pouch = {"Cherry Bombs": 0, "Datura Bombs": 0, "Smoke Decoy Bombs": 0}

while bomb_effects and bomb_casings and not is_pouch_filled(pouch):
    value = bomb_effects[0] + bomb_casings[-1]
    if value not in materials:
        bomb_casings[-1] -= 5
        continue

    bomb_name = materials[value]
    pouch[bomb_name] += 1
    bomb_effects.popleft()
    bomb_casings.pop()

print(get_result_message(pouch))
print(f"Bomb Effects: {get_collection_result(bomb_effects)}")
print(f"Bomb Casings: {get_collection_result(bomb_casings)}")
print(get_bomb_pouch_result(pouch))
