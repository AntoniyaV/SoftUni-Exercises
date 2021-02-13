def palindrome(word, index=0, end_index=-1):
    if index == len(word) // 2:
        return f"{word} is a palindrome"

    if word[index] == word[end_index]:
        return palindrome(word, index + 1, end_index - 1)
    else:
        return f"{word} is not a palindrome"


print(palindrome("abba", 0))
print(palindrome("peter", 0))
