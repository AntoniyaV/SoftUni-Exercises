import re

text = input()
word = input()
pattern = rf"\b{word}\b"

matches = re.findall(pattern, text, re.I)

print(len(matches))
