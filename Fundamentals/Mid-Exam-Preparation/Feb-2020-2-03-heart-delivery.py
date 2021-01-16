neighbourhood = input().split("@")
command = input()

neighbourhood = [int(i) for i in neighbourhood]
index = 0

while not command == "Love!":
    length = int(command.split()[1])
    index += length
    if index >= len(neighbourhood):
        index = 0

    if neighbourhood[index] == 0:
        print(f"Place {index} already had Valentine's day.")

    else:
        neighbourhood[index] -= 2
        if neighbourhood[index] <= 0:
            neighbourhood[index] = 0
            print(f"Place {index} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {index}.")

if sum(neighbourhood) == 0:
    print("Mission was successful.")

else:
    failed_houses = [n for n in neighbourhood if not n == 0]
    print(f"Cupid has failed {len(failed_houses)} places.")

