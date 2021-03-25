def number_increment(numbers):
    def increase():
        new_numbers = [num + 1 for num in numbers]
        return new_numbers
    return increase()


# Test code:
print(number_increment([1, 2, 3]))
