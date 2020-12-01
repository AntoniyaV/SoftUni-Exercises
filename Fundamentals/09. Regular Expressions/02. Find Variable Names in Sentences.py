import re
text = input()
pattern = r"((?<=^_)|(?<=\s_))[A-Za-z0-9]+($|(?=\s))"
matches = re.finditer(pattern, text)

print(','.join([match.group() for match in matches]))