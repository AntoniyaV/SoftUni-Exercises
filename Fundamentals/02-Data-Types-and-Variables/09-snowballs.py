snowballs_num = int(input())

snowball_value = 0
highest_value = 0
highest_snow = 0
highest_time = 0
highest_quality = 0

for i in range(1, snowballs_num + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = int((snowball_snow / snowball_time) ** snowball_quality)

    if snowball_value > highest_value:
        highest_value = snowball_value
        highest_snow = snowball_snow
        highest_time = snowball_time
        highest_quality = snowball_quality

print(f"{highest_snow} : {highest_time} = {highest_value} ({highest_quality})")