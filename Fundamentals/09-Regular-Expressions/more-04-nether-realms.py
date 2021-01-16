import re

demon_names = input().split(',')
demon_names = [n.strip() for n in demon_names]

demons = {}

for name in demon_names:

    char_matches = re.findall(r'[^0-9\+\*\./-]', name)
    demon_health = sum([ord(sym) for sym in char_matches])

    number_matches = re.finditer(r'[\+-]?\d+(\.\d+)?', name)
    demon_damage = sum([float(match.group()) for match in number_matches])

    for char in name:
        if char == "*":
            demon_damage *= 2
        elif char == "/":
            demon_damage /= 2

    demons[name] = [demon_health, demon_damage]

sorted_demons = sorted(demons.items(), key=lambda x: x[0])

for demon in sorted_demons:
    print(f"{demon[0]} - {demon[1][0]} health, {demon[1][1]:.2f} damage")
