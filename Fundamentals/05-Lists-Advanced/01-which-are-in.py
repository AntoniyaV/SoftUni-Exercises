first_list = input().split(", ")
second_list = input().split(", ")

result = []

for word_1 in first_list:
    for word_2 in second_list:
        if word_1 in word_2:
            result.append(word_1)
            break

print(result)