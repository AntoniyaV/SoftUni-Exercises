def vowel_filter(function):

    def wrapper():
        vowels = {"a", "e", "i", "o", "u", "y"}
        result = function()
        filtered_vowels = [el for el in result if el.lower() in vowels]
        return filtered_vowels
    return wrapper


# Test code:
@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
