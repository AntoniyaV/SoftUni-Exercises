import re

text = input()

pattern = r"%(?P<customer>[A-Z][a-z]+)%.*?<(?P<product>\w+)>.*?\|(?P<count>\d+)\|.*?(?P<price>\d+(\.\d+)?)\$"
total_income = 0

while not text == "end of shift":
    valid_line = re.finditer(pattern, text)
    for line in valid_line:
        customer_info = line.groupdict()
        customer_total = int(customer_info['count']) * float(customer_info['price'])

        print(f"{customer_info['customer']}: {customer_info['product']} - {customer_total:.2f}")

        total_income += customer_total

    text = input()

print(f"Total income: {total_income:.2f}")