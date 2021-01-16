def loading_bar(number):
    if number == 0:
        print("0% [..........]")
        print("Still loading...")

    elif number == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")

    else:
        counter = int(number / 10)
        percent_str = ""

        for count in range(counter):
            percent_str += "%"

        for left_count in range(counter + 1, 11):
            percent_str += "."

        print(f"{number}% [{percent_str}]")
        print("Still loading...")


num = int(input())
loading_bar(num)
