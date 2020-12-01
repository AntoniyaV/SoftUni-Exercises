quantity = int(input())
days = int(input())

ornament_set = 0
skirts = 0
garlands = 0
lights = 0
total_spirit = 0

for i in range(1, days + 1):
    spirit = 0
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        ornament_set += quantity
        spirit += 5
    if i % 3 == 0:
        skirts += quantity
        garlands += quantity
        spirit += 13
    if i % 5 == 0:
        lights += quantity
        spirit += 17
    if i % 3 == 0 and i % 5 == 0:
        spirit += 30
    if i % 2 == 0 and i % 5 == 0:
        spirit -= 20
        skirts += 1
        garlands += 1
        lights += 1

    total_spirit += spirit

if days % 2 == 0 and days % 5 == 0:
    total_spirit -= 30

total_cost = ornament_set * 2 + skirts * 5 + garlands * 3 + lights * 15
print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")