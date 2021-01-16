word_one, word_two = input().split()

result = 0
end = 0

if len(word_one) >= len(word_two):
    end = len(word_one)
else:
    end = len(word_two)

for i in range(end):
    if i in range(len(word_one)) and i in range(len(word_two)):
        result += (ord(word_one[i]) * ord(word_two[i]))
    else:
        if i in range(len(word_one)):
            result += ord(word_one[i])
        elif i in range(len(word_two)):
            result += ord(word_two[i])

print(result)