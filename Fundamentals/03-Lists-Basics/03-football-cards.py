team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

cards = input()
cards_list = cards.split()

for element in cards_list:
    single_card = element.split("-")
    player = int(single_card[1])

    if "A" in element:
        if player in team_a:
            team_a.remove(player)
    elif "B" in element:
        if player in team_b:
            team_b.remove(player)

    if len(team_a) < 7 or len(team_b) < 7:
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")

if len(team_a) < 7 or len(team_b) < 7:
    print("Game was terminated")
