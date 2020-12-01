data = input().split()
result = 0

for el in data:
    first_letter = el[0]
    first_letter_position = ord(el[0].lower()) - 96
    last_letter = el[-1]
    last_letter_position = ord(el[-1].lower()) - 96
    number = int(el[1:len(el) - 1])

    if first_letter.isupper():
        number /= first_letter_position
    else:
        number *= first_letter_position

    if last_letter.isupper():
        number -= last_letter_position
    else:
        number += last_letter_position

    result += number

print(f"{result:.2f}")
