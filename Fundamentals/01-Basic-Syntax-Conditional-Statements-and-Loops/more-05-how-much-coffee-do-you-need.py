command = input()

num_coffees = 0

while not command == "END":
    if command == "coding" or command == "cat" or command == "dog" or command == "movie":
        num_coffees += 1
    elif command == "CODING" or command == "CAT" or command == "DOG" or command == "MOVIE":
        num_coffees += 2

    if num_coffees > 5:
        print("You need extra sleep")
        break

    command = input()

if num_coffees <= 5:
    print(num_coffees)
