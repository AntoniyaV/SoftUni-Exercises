class vowels:
    vowels = {"a", "e", "i", "o", "u", "y"}

    def __init__(self, string):
        self.string = string
        self.i = 0
        self.n = len(self.string)

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration()

        i = self.i
        self.i += 1
        if self.string[i].lower() not in self.vowels:
            return self.__next__()
        return self.string[i]


# Test code:
my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
