name = input()

time = 0
gold_cards = 0
silver_cards = 0
bronze_cards = 0

winner_time = 1000
winner_name = ""

while name != "Finish":
    minutes = int(input())
    seconds = int(input())

    time = minutes * 60 + seconds
    if time < 55:
        gold_cards += 1
    elif 55 <= time <= 85:
        silver_cards += 1
    elif 85 < time <= 120:
        bronze_cards += 1

    if time < winner_time:
        winner_time = time
        winner_name = name

    name = input()

print(f"With {winner_time // 60} minutes and {winner_time % 60} seconds {winner_name} is the winner of the day!")
print(f"Today's prizes are {gold_cards} Gold {silver_cards} Silver and {bronze_cards} Bronze cards!")