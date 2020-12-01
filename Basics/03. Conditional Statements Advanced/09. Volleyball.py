year_type = input()
p = int(input())
h = int(input())

at_home = 48 - h
not_working = at_home * (3/4)
holiday_play = p * (2/3)
games_count = not_working + holiday_play + h

if year_type == "leap":
    games_count += games_count * 0.15

import math
games_count = math.floor(games_count)

print(games_count)