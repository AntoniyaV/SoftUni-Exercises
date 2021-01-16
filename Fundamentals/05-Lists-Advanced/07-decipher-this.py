def decipher_words(list_of_words):
    new_list = []

    for word in list_of_words:
        elements = list(word)
        new_word = []

        ints = [n for n in elements if n.isdigit()]
        ints_str = list(map(lambda ch: str(ch), ints))
        number = int("".join(ints_str))
        first_letter = chr(number)
        new_word.append(first_letter)

        letters = [letter for letter in elements if letter.isalpha()]
        letters[0], letters[-1] = letters[-1], letters[0]
        new_word.extend(letters)

        new_word = "".join(new_word)
        new_list.append(new_word)

    return new_list


words = input().split()

new_words = decipher_words(words)
deciphered = " ".join(new_words)

print(deciphered)
