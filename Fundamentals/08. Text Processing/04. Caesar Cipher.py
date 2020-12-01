message = input()
encrypted = ""

for el in message:
    encrypted += chr(ord(el) + 3)

print(encrypted)