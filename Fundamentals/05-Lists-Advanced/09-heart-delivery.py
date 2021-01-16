neighbourhood = input().split("@")
neighbourhood = [int(n) for n in neighbourhood]

command = input()
index = 0
last_pos = 0

while not command == "Love!":
    jump, length = command.split()
    length = int(length)

    index += length

    if index > len(neighbourhood) - 1:
        index = 0
        last_pos = length

    if neighbourhood[index] == 0:
        print(f"Place {index} already had Valentine's day.")
    else:
        neighbourhood[index] -= 2
        if neighbourhood[index] <= 0:
            neighbourhood[index] = 0
            print(f"Place {index} has Valentine's day.")

    last_pos = index
    command = input()

print(f"Cupid's last position was {last_pos}.")

if all(el == 0 for el in neighbourhood):
    print("Mission was successful.")

else:
    failed_houses = [house for house in neighbourhood if not house == 0]
    print(f"Cupid has failed {len(failed_houses)} places.")