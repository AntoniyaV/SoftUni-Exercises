def is_valid(word):
    return len(word) % 2 == 0


def filtered_words(words):
    return [w for w in words if is_valid(w)]


def print_result(result):
    return [print(wrd) for wrd in result]


text = input().split()
filtered = filtered_words(text)
print_result(filtered)
