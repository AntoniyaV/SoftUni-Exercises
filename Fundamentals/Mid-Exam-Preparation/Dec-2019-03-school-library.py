books = input().split("&")
command = input()

while not command == "Done":
    book_name = command.split(" | ")[1]

    if "Add" in command and book_name not in books:
        books.insert(0, book_name)

    elif "Take" in command and book_name in books:
        books.remove(book_name)

    elif "Swap" in command and book_name in books:
        book_name_2 = command.split(" | ")[2]
        if book_name_2 in books:
            index_1 = books.index(book_name)
            index_2 = books.index(book_name_2)
            books[index_1], books[index_2] = book_name_2, book_name

    elif "Insert" in command:
        books.append(book_name)

    elif "Check" in command:
        index = int(command.split(" | ")[1])
        if index in range(len(books)):
            print(books[index])

    command = input()

print(", ".join(books))