info = input()
cities = {}

while not info == "Sail":
    city, population, gold = info.split("||")
    population, gold = int(population), int(gold)

    if city not in cities:
        cities[city] = {"population": population, "gold": gold}
    else:
        cities[city]["population"] += population
        cities[city]["gold"] += gold

    info = input()


def plunder_town(some_event, some_dict, some_town):
    people, stolen_gold = int(some_event.split("=>")[2]), int(some_event.split("=>")[3])

    some_dict[some_town]["population"] -= people
    some_dict[some_town]["gold"] -= stolen_gold

    print(f"{some_town} plundered! {stolen_gold} gold stolen, {people} citizens killed.")

    if some_dict[some_town]["population"] <= 0 or some_dict[some_town]["gold"] <= 0:
        some_dict.pop(some_town)
        print(f"{some_town} has been wiped off the map!")

    return some_dict


def prosper_town(some_event, some_dict, some_town):
    added_gold = int(some_event.split("=>")[2])

    if added_gold < 0:
        print("Gold added cannot be a negative number!")
        return some_dict

    some_dict["gold"] += added_gold
    print(f"{added_gold} gold added to the city treasury. {some_town} now has {some_dict['gold']} gold.")

    return some_dict


events = input()

while not events == "End":
    action, town = events.split("=>")[0], events.split("=>")[1]

    if action == "Plunder":
        cities = plunder_town(events, cities, town)

    elif action == "Prosper":
        cities[town] = prosper_town(events, cities[town], town)

    events = input()

if cities:
    sorted_cities = dict(sorted(cities.items(), key=lambda x: (-x[1]['gold'], x[0])))
    print(f"Ahoy, Captain! There are {len(sorted_cities)} wealthy settlements to go to:")

    for sorted_city, city_values in sorted_cities.items():
        print(f"{sorted_city} -> Population: {city_values['population']} citizens, Gold: {city_values['gold']} kg")

else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")