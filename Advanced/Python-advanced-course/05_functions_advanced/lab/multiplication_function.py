def multiply(*args):
    result = 1
    for n in args:
        result *= n
    return result

print(multiply(2, 0, 1000, 5000))