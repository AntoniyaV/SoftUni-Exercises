def multiply(times):
    def decorator(function):
        def wrapper(number):
            num = function(number)
            res = num * times
            return res
        return wrapper
    return decorator


# Test code:
@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))


@multiply(5)
def add_ten(number):
    return number + 10

print(add_ten(6))
