import re
text = input()
pattern = r">>(?P<name>[A-Za-z]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)"
bought_items = []
total_price = 0

while not text == "Purchase":
    matches = re.finditer(pattern, text)
    for match in matches:
        bought_items.append(match.group('name'))
        total_price += float(match.group('price')) * int(match.group('quantity'))

    text = input()

print("Bought furniture:")
for item in bought_items:
    print(item)
print(f"Total money spend: {total_price:.2f}")