import re
num_messages = int(input())
messages = []

for n in range(num_messages):
    messages.append(input())

attacked_planets = []
destroyed_planets = []
pattern = r'@(?P<planet>[a-zA-Z]+)[^@!:>-]*?:(?P<population>\d+)[^@!:>-]*?!(?P<type>[AD])![^@!:>-]*?->(?P<soldiers>\d+)'

for message in messages:
    letter_matches = re.findall(r'[star]', message, re.I)
    counter = len(letter_matches)
    decrypted = ''.join([chr(ord(sym) - counter) for sym in message])

    planet_matches = re.finditer(pattern, decrypted)

    for match in planet_matches:
        planet_info = match.groupdict()

        if planet_info['type'] == "A":
            attacked_planets.append(planet_info['planet'])

        elif planet_info['type'] == "D":
            destroyed_planets.append(planet_info['planet'])


print(f"Attacked planets: {len(attacked_planets)}")
for planet in sorted(attacked_planets):
    print(f"-> {planet}")

print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in sorted(destroyed_planets):
    print(f"-> {planet}")
