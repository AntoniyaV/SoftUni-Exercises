number = input()

list_number = list(number)
list_number.sort(reverse=True)

new_number = ""

for i in list_number:
    new_number += i

print(new_number)