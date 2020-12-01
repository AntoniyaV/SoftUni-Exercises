import re
text = input()
pattern = r"www\.[a-zA-Z0-9-]+(\.[a-z]+)+"
matches = []

while text:
    matches = re.finditer(pattern, text)
    for match in matches:
        print(match.group())

    text = input()