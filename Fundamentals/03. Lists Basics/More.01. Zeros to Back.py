str_numbers = input()
numbers = str_numbers.split(", ")
numbers = [int(i) for i in numbers]

for el in numbers:
    if el == 0:
        numbers.remove(0)
        numbers.append(0)

print(numbers)