numbers_str = input()
num_beggars = int(input())

numbers_list = numbers_str.split(", ")
sums_list = []

for person in range(1, num_beggars + 1):
    sum = 0
    for index in range(person - 1, len(numbers_list), num_beggars):
        sum += int(numbers_list[index])
    sums_list.append(sum)

print(sums_list)
