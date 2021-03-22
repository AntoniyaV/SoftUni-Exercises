def genrange(start, end):
    i = start
    while i <= end:
        yield i
        i += 1

# Test code:
print(list(genrange(1, 10)))
