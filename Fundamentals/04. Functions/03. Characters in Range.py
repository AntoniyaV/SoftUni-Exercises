def characters_in_range(char1, char2):
    chars_str = ''
    for i in range(ord(char1) + 1, ord(char2)):
        chars_str += chr(i) + " "

    return chars_str


character_1 = input()
character_2 = input()

print(characters_in_range(character_1, character_2))