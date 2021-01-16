numbers = input().split()
some_text = list(input())

message = ""

for num in numbers:
    index = 0

    for digit in num:
        index += int(digit)

    if index >= len(some_text):
        index -= len(some_text)

    message += some_text[index]
    some_text.pop(index)

print(message)