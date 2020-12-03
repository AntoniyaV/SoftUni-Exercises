import re

text = input()

num_matches = re.findall("\\d", text)
num_matches = [int(n) for n in num_matches]

cool_threshold = 1
for num in num_matches:
    cool_threshold *= num

emoji_pattern = r"(::|\*\*)[A-Z][a-z]{2,}\1"
valid_emojis = re.finditer(emoji_pattern, text)

cool_emojis = []
count_emojis = 0

for emoji in valid_emojis:
    count_emojis += 1
    coolness = sum([ord(ch) for ch in emoji.group() if ch.isalpha()])

    if coolness >= cool_threshold:
        cool_emojis.append(emoji.group())

print(f"Cool threshold: {cool_threshold}")

print(f"{count_emojis} emojis found in the text. The cool ones are:")

if cool_emojis:
    for cool_e in cool_emojis:
        print(cool_e)
