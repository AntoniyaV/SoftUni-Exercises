fav_book = input()
book_name = input()

num_books = 0

while book_name != fav_book:
    if book_name == "No More Books":
        break
    num_books += 1
    book_name = input()

if book_name == fav_book:
    print(f"You checked {num_books} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {num_books} books.")