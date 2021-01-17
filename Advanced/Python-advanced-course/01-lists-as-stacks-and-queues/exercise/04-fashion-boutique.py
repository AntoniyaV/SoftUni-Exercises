<<<<<<< HEAD
clothes = [int(x) for x in input().split()]
capacity = int(input())

number_of_racks = 1
sum_values = 0

while clothes:
    current_clothing = clothes[-1]
    sum_values += current_clothing

    if sum_values < capacity:
        clothes.pop()

    elif sum_values == capacity:
        clothes.pop()
        if clothes:
            number_of_racks += 1
            sum_values = 0

    else:
        number_of_racks += 1
        sum_values = 0

print(number_of_racks)
=======
clothes = [int(x) for x in input().split()]
capacity = int(input())

number_of_racks = 1
sum_values = 0

while clothes:
    current_clothing = clothes[-1]
    sum_values += current_clothing

    if sum_values < capacity:
        clothes.pop()

    elif sum_values == capacity:
        clothes.pop()
        if clothes:
            number_of_racks += 1
            sum_values = 0

    else:
        number_of_racks += 1
        sum_values = 0

print(number_of_racks)
>>>>>>> c6ab6c831ddfde4b18aa1def9039f6cda9cb6b84
