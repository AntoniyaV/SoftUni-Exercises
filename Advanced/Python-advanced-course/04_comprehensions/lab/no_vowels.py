def remove_vowels(some_text, some_vowels):
    return [letter for letter in some_text if letter not in some_vowels]


text = input()

vowels = ['a', 'o', 'u', 'e', 'i']
vowels += [vow.upper() for vow in vowels]

no_vowels = remove_vowels(text, vowels)
print(''.join(no_vowels))
