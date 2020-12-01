def get_legendary_item(some_material):
    legendary = ""

    if some_material == "shards":
        legendary = "Shadowmourne"

    elif some_material == "fragments":
        legendary = "Valanyr"

    elif some_material == "motes":
        legendary = "Dragonwrath"

    return legendary


key_materials = {"fragments": 0, "motes": 0, "shards": 0}
junk = {}
legendary_item = ""

while legendary_item == "":
    materials = input().split()

    for i in range(0, len(materials), 2):
        key = materials[i + 1].lower()
        value = int(materials[i])

        if key in key_materials:
            key_materials[key] += value

            if key_materials[key] >= 250:
                legendary_item = get_legendary_item(key)
                key_materials[key] -= 250
                break

        else:
            if key not in junk:
                junk[key] = 0
            junk[key] += value

print(f"{legendary_item} obtained!")

sorted_materials = dict(sorted(key_materials.items(), key=lambda x: x[1], reverse=True))
for key, value in sorted_materials.items():
    print(f"{key}: {value}")

sorted_junk = dict(sorted(junk.items(), key=lambda x: x[0]))
for key, value in sorted_junk.items():
    print(f"{key}: {value}")
