string_of_nums = input()
list_of_nums = string_of_nums.split(" ")
opposite = []

for i in list_of_nums:
    number = int(i)
    if number > 0:
        opposite.append(-number)
    elif number < 0:
        opposite.append(abs(number))
    else:
        opposite.append(number)

print(opposite)