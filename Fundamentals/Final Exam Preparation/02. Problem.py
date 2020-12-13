import re

num_lines = int(input())
pattern = r'^(.+)>(?P<numbers>\d{3})\|(?P<lower>[a-z]{3})\|(?P<upper>[A-Z]{3})\|(?P<symbols>[^<>]{3})<\1$'

for n in range(num_lines):
    password = input()

    if not re.match(pattern, password):
        print("Try another password!")
        continue

    matches = re.finditer(pattern, password)
    valid_password = ""

    for match in matches:
        info = match.groupdict()
        valid_password = info['numbers'] + info['lower'] + info['upper'] + info['symbols']

    print(f"Password: {valid_password}")
