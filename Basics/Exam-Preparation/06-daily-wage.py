lines = int(input())
positions = int(input())

price_strawberries = 3.50
price_blueberries = 5.00

strawberries = 0
blueberries = 0

for line in range(1, lines + 1):
    if line % 2 != 0:
        strawberries += positions
    else:
        for position in range(1, positions + 1):
            if position % 3 != 0:
                blueberries += 1

total_price = strawberries * price_strawberries + blueberries * price_blueberries
total_price = total_price * 0.8
print(f"Total: {total_price:.2f} lv.")