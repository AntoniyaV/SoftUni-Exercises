word = input()
letters_indices = []

for i in range(0, len(word)):
    if word[i].isupper():
        letters_indices.append(i)

print(letters_indices)


# Грешно решение в judge:

# word = input()
# letters_indices = []
# position = -1
#
# for i in word:
#     position += 1
#     if i == i.upper():
#         letters_indices.append(position)
#
# print(letters_indices)