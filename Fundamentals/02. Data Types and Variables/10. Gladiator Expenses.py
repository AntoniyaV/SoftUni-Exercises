lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

shield_count = 0
money_needed = 0

for i in range(1, lost_fights + 1):
    if i % 2 == 0:
        money_needed += helmet_price
    if i % 3 == 0:
        money_needed += sword_price
        if i % 2 == 0:
            money_needed += shield_price
            shield_count += 1
            if shield_count % 2 == 0:
                money_needed += armor_price

print(f"Gladiator expenses: {money_needed:.2f} aureus")
