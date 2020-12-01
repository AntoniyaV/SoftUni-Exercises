budget = float(input())
flour_price = float(input())

eggs_price = 0.75 * flour_price
milk_price = (flour_price + (0.25 * flour_price)) / 4
cozonac_price = eggs_price + flour_price + milk_price

colored_eggs = 0
cozonac_count = 0
lost_eggs = 0

while budget > cozonac_price:
    colored_eggs += 3
    cozonac_count += 1
    if cozonac_count % 3 == 0:
       lost_eggs = cozonac_count - 2
       colored_eggs -= lost_eggs
    budget -= cozonac_price

print(f"You made {cozonac_count} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")