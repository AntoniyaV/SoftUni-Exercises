def type_check(type_name):
    def decorator(func):
        def wrapper(arg):
            if not type(arg) == type_name:
                return "Bad Type"
            return func(arg)
        return wrapper
    return decorator


# Test code:
@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))

