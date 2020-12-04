import re

text = input()
pattern = r"(\||#)(?P<item>[A-Za-z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>([0-9][0-9]{0,3}|10000))\1"
valid_items = re.finditer(pattern, text)

all_foods = []
total_calories = 0

for item in valid_items:
    current_item = item.groupdict()
    total_calories += int(current_item['calories'])
    all_foods.append(current_item)

print(f"You have food to last you for: {total_calories // 2000} days!")

for food in all_foods:
    print(f"Item: {food['item']}, Best before: {food['date']}, Nutrition: {food['calories']}")