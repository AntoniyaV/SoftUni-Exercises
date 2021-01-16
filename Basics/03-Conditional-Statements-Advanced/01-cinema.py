screening_type = input()
rows = int(input())
columns = int(input())
if screening_type == "Premiere":
    print(f"{rows * columns * 12.00:.2f} leva")
elif screening_type == "Normal":
    print(f"{rows * columns * 7.50:.2f} leva")
elif screening_type == "Discount":
        print(f"{rows * columns * 5.00:.2f} leva")