words = list(input())
symbols = {}

for char in words:
    if not char == " ":

        if char not in symbols:
            symbols[char] = 0

        symbols[char] += 1

for key, value in symbols.items():
    print(f"{key} -> {value}")