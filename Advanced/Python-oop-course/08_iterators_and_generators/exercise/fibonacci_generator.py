def fibonacci():
    previous_num = 0
    current_num = 1

    yield previous_num
    yield current_num

    while True:
        res = previous_num + current_num
        yield res

        previous_num = current_num
        current_num = res


# Test code:
generator = fibonacci()
for i in range(5):
    print(next(generator))
