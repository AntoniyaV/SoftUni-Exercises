from time import process_time


def exec_time(func):
    def wrapper(*args):
        start = process_time()
        func(*args)
        end = process_time() - start
        return end
    return wrapper


# Test code:
@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total
print(loop(1, 10000000))



@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result
print(concatenate(["a" for i in range(1000000)]))
