key = int(input())
n = int(input())

new_char = ''
new_word = ''

for i in range(1, n + 1):
    char = input()
    new_char = ord(char) + key
    new_word += chr(new_char)

print(new_word)