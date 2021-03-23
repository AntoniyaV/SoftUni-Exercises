class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.number = 0
        self.numbers_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.numbers_count == self.count:
            raise StopIteration()

        num = self.number
        self.number += self.step
        self.numbers_count += 1
        return num


# Test code:
numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)

