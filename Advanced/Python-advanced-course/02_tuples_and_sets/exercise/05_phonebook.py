def add_data_to_phonebook(data, book):
    name, phone = data.split('-')

    if name not in book:
        book[name] = ''

    book[name] = phone

    return book


phonebook = {}
n = 0

while True:
    info = input()

    if info.isdigit():
        n = int(info)
        break

    phonebook = add_data_to_phonebook(info, phonebook)

for _ in range(n):
    contact = input()

    if contact in phonebook:
        print(f'{contact} -> {phonebook[contact]}')
    else:
        print(f'Contact {contact} does not exist.')
