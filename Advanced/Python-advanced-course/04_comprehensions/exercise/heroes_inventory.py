def add_to_inventory(name, item, cost, inventory):
    if item not in inventory[name]:
        inventory[name][item] = int(cost)
    return inventory


def print_result(result):
    return [print(f"{name} -> Items: {len(items)}, Cost: {sum([items[item] for item in items])}") for name, items in result.items()]


heroes_inventory = {hero: {} for hero in input().split(', ')}

while True:
    info = input()
    if info == 'End':
        break

    hero_name, hero_item, hero_item_cost = info.split('-')
    heroes_inventory = add_to_inventory(hero_name, hero_item, hero_item_cost, heroes_inventory)

print_result(heroes_inventory)
