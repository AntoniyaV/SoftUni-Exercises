some_text = input()

digits = [n for n in some_text if n.isdigit()]

non_digits = [el for el in some_text if not el.isdigit()]
take_list = [int(digits[i]) for i in range(len(digits)) if i % 2 == 0]
skip_list = [int(digits[j]) for j in range(len(digits)) if not j % 2 == 0]

hidden_message = ""
skip = 0
index = 0


for take in take_list:
    index += 1
    current_turn = 0

    for char in range(skip, len(non_digits)):
        if current_turn == take:
            break
        hidden_message += non_digits[char]
        current_turn += 1

    skip += skip_list[index - 1] + take

print(hidden_message)
