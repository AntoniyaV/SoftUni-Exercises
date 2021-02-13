def operate(operator, *args):
    result = args[0]
    if operator == '+':
        result = sum(args)
    elif operator == '-':
        for i in range(1, len(args)):
            result -= args[i]
    elif operator == '*':
        for i in range(1, len(args)):
            result *= args[i]
    elif operator == '/':
        for i in range(1, len(args)):
            result /= args[i]
    return result

print(operate("/", 3, 4))