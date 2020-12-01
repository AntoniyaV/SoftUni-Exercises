num_heroes = int(input())
heroes = {}

for n in range(num_heroes):
    hero, hit, mana = input().split()
    hit, mana = int(hit), int(mana)

    heroes[hero] = {"HP": hit, "MP": mana}

command = input()


def cast_spell(some_command, some_dict):
    hero_name, mp_needed, spell_name = command.split(" - ")[1], int(some_command.split(" - ")[2]), some_command.split(" - ")[3]

    if some_dict[hero_name]["MP"] >= mp_needed:
        some_dict[hero_name]["MP"] -= mp_needed
        print(f"{hero_name} has successfully cast {spell_name} and now has {some_dict[hero_name]['MP']} MP!")

    else:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    return some_dict


def take_damage(some_command, some_dict):
    hero_name, damage, attacker = command.split(" - ")[1], int(some_command.split(" - ")[2]), some_command.split(" - ")[3]

    if some_dict[hero_name]["HP"] > damage:
        some_dict[hero_name]["HP"] -= damage
        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {some_dict[hero_name]['HP']} HP left!")

    else:
        some_dict.pop(hero_name)
        print(f"{hero_name} has been killed by {attacker}!")

    return some_dict


def recharge(some_command, some_dict):
    hero_name, amount = command.split(" - ")[1], int(some_command.split(" - ")[2])

    some_dict[hero_name]["MP"] += amount

    if some_dict[hero_name]["MP"] > 200:
        amount -= some_dict[hero_name]["MP"] - 200
        some_dict[hero_name]["MP"] = 200

    print(f"{hero_name} recharged for {amount} MP!")

    return some_dict


def heal(some_command, some_dict):
    hero_name, amount = command.split(" - ")[1], int(some_command.split(" - ")[2])

    some_dict[hero_name]["HP"] += amount

    if some_dict[hero_name]["HP"] > 100:
        amount -= some_dict[hero_name]["HP"] - 100
        some_dict[hero_name]["HP"] = 100

    print(f"{hero_name} healed for {amount} HP!")

    return some_dict

while not command == "End":
    action = command.split(" - ")[0]

    if action == "CastSpell":
        heroes = cast_spell(command, heroes)

    elif action == "TakeDamage":
        heroes = take_damage(command, heroes)

    elif action == "Recharge":
        heroes = recharge(command, heroes)

    elif action == "Heal":
        heroes = heal(command, heroes)

    command = input()

sorted_heroes = dict(sorted(heroes.items(), key=lambda x: (-x[1]['HP'], x[0])))

for key, value in sorted_heroes.items():
    print(key)
    print(f"  HP: {value['HP']}")
    print(f"  MP: {value['MP']}")