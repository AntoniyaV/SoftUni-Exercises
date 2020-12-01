single_string = input()
list_animals = single_string.split(", ")

sheep_counter = 0

for animal in range(len(list_animals) - 1, -1, -1):
    if list_animals[animal] == "sheep":
        sheep_counter += 1
    if list_animals[animal] == "wolf":
        if animal == len(list_animals) - 1:
            print("Please go away and stop eating my sheep")
            break
        else:
            print(f"Oi! Sheep number {sheep_counter}! You are about to be eaten by a wolf!")
            break
