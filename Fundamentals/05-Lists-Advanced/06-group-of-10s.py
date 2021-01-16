numbers = input().split(", ")
numbers = list(map(lambda n: int(n), numbers))

boundary = 10

while len(numbers) > 0:
    group_list = [num for num in numbers if num <= boundary]

    for n in group_list:
        if n in numbers:
            numbers.remove(n)

    print(f"Group of {boundary}'s: {group_list}")

    boundary += 10
