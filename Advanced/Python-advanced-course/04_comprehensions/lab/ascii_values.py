def get_character_value(list_of_chars):
    return {x: ord(x) for x in list_of_chars}


characters = input().split(', ')

char_value = get_character_value(characters)
print(char_value)