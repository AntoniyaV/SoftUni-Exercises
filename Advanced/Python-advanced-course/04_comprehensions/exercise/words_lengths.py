def words_lengths(words):
    return [word + ' -> ' + str(len(word)) for word in words]


text = input().split(', ')

words_with_lengths = words_lengths(text)
print(', '.join(words_with_lengths))