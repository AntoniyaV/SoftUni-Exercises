import re
text = input()
pattern = r"(^|(?<=\s))[a-z0-9][a-z0-9._-]+[a-z0-9]@[a-z][a-z-]+(\.[a-z][a-z-]+)+"
matches = re.finditer(pattern, text)

for match in matches:
    print(match.group())