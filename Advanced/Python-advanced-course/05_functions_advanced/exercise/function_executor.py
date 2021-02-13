def func_executor(*args):
    results = []
    for pair in args:
        func = pair[0]
        elements = pair[1]
        result = func(*elements)
        results.append(result)
    return results


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
