number_one = int(input())
number_two = int(input())
op = input()

result = 0

if op == "+" or op == "-" or op == "*":
    if op == "+":
        result = number_one + number_two
    elif op == "-":
        result = number_one - number_two
    elif op == "*":
        result = number_one * number_two
    if result % 2 == 0:
        print(f"{number_one} {op} {number_two} = {result} - even")
    else:
        print(f"{number_one} {op} {number_two} = {result} - odd")
elif op == "/":
    if number_two != 0:
        result = number_one / number_two
        print(f"{number_one} {op} {number_two} = {result:.2f}")
    else:
        print(f"Cannot divide {number_one} by zero")
elif op == "%":
    if number_two != 0:
        result = number_one % number_two
        print(f"{number_one} {op} {number_two} = {result}")
    else:
        print(f"Cannot divide {number_one} by zero")