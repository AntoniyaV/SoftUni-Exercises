party_size = int(input())
days = int(input())

coins_gained = 0
coins_spent = 0

for i in range(1, days + 1):
    if i % 10 == 0:
        party_size -= 2
    if i % 15 == 0:
        party_size += 5

    coins_gained += 50
    coins_spent += 2 * party_size

    if i % 3 == 0:
        coins_spent += 3 * party_size
    if i % 5 == 0:
        coins_gained += 20 * party_size
        if i % 3 == 0:
            coins_spent += 2 * party_size

total_coins = coins_gained - coins_spent
coins_per_person = int(total_coins / party_size)

print(f"{party_size} companions received {coins_per_person} coins each.")