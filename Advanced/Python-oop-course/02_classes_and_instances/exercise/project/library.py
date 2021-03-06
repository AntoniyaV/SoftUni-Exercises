class Library:
    user_records = []
    books_available = {}
    rented_books = {}


    def add_user(self, user):
        if user in Library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        Library.user_records.append(user)

    def remove_user(self, user):
        if user not in Library.user_records:
            return "We could not find such user to remove!"

        Library.user_records.remove(user)

        if user.username in Library.rented_books:
            del Library.rented_books[user.username]

    def change_username(self, user_id, new_username):
        matched_user = [user for user in Library.user_records if user.user_id == user_id]
        if not matched_user:
            return f"There is no user with id = {user_id}!"

        matched_user = matched_user[0]
        if matched_user.username == new_username:
            return "Please check again the provided username - it should be different than the username used so far!"

        if matched_user.username in Library.rented_books:
            Library.rented_books[new_username] = Library.rented_books[matched_user.username]
            del Library.rented_books[matched_user.username]

        matched_user.username = new_username
        return f"Username successfully changed to: {new_username} for userid: {user_id}"
