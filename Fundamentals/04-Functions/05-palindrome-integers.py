def palindrome_integer_checker(ints):
    ints_list = ints.split(", ")

    for element in ints_list:
        rev_element = ""

        for symbol in range(len(element) - 1, -1, -1):
            rev_element += element[symbol]

        if rev_element == element:
            print("True")
        else:
            print("False")


str_ints = input()
palindrome_integer_checker(str_ints)