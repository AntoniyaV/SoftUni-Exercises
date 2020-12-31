players = {}
total_points = {}

info = input()

while not info == "Season end":
    if "->" in info:
        player, position, skill = info.split(" -> ")
        skill = int(skill)

        if player not in players:
            players[player] = {}

        if position not in players[player] or players[player][position] < skill:
            players[player][position] = skill

        if player not in total_points:
            total_points[player] = 0

    else:
        player_1, player_2 = info.split(" vs ")

        if player_1 and player_2 in players:
            for pos, pos_skill in players[player_1].items():
                if pos in players[player_2]:

                    if players[player_1][pos] < players[player_2][pos]:
                        players.pop(player_1)
                        total_points.pop(player_1)

                    elif players[player_1][pos] > players[player_2][pos]:
                        players.pop(player_2)
                        total_points.pop(player_2)

                    break

    info = input()

for plyr, positions in players.items():
    for plyr_pos, pos_skl in positions.items():
        total_points[plyr] += pos_skl

sorted_total = dict(sorted(total_points.items(), key=lambda x: (-x[1], x[0])))

for person, total_skill in sorted_total.items():
    print(f"{person}: {total_skill} skill")

    sorted_player = dict(sorted(players[person].items(), key=lambda x: (-x[1], x[0])))
    for player_pos, position_skill in sorted_player.items():
        print(f"- {player_pos} <::> {position_skill}")