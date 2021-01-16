import re
text = input()
pattern = r"\d+"
matches = []

while text:
    matches += re.findall(pattern, text)
    text = input()

print(' '.join(matches))