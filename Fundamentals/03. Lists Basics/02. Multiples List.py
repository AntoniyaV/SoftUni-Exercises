factor = int(input())
count = int(input())

nums_list = []
number = 0

while len(nums_list) < count:
    number += 1
    if number % factor == 0:
        nums_list.append(number)

print(nums_list)
