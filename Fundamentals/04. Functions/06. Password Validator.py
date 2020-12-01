def password_validator(pswd):
    good_pswd = True

    if not 6 <= len(pswd) <= 10:
        print("Password must be between 6 and 10 characters")
        good_pswd = False

    digit_count = 0
    special_char = 0

    for sym in pswd:
        if not (48 <= ord(sym) <= 57 or 65 <= ord(sym) <= 90 or 97 <= ord(sym) <= 122):
            special_char += 1

        if 48 <= ord(sym) <= 57:
            digit_count += 1

    if not special_char == 0:
        print("Password must consist only of letters and digits")
        good_pswd = False

    if digit_count < 2:
        print("Password must have at least 2 digits")
        good_pswd = False

    if good_pswd:
        print("Password is valid")


password = input()
password_validator(password)
