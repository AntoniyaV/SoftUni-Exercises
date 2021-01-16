import re

number = int(input())
pattern = r"^@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+$"

for num in range(number):
    barcode = input()
    valid = re.match(pattern, barcode)

    if valid:
        group = [n for n in barcode if n.isdigit()]
        if group:
            group = ''.join(group)
        else:
            group = '00'
        print(f"Product group: {group}")

    else:
        print("Invalid barcode")
