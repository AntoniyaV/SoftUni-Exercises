class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.number - 1:
            raise StopIteration()

        symbol = self.sequence[self.index]
        self.index += 1
        self.sequence += symbol
        return symbol


# Test code:
result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
