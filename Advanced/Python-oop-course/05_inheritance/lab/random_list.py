import random


class RandomList(list):
    def get_random_element(self):
        random_element = random.choice(self)
        self.remove(random_element)
        return random_element


# Test code
some_list = RandomList([1, 3, 5, 'a', 'ok', 'hi', 8.9, True, [1, 4, 6]])
print(some_list.get_random_element())
print(some_list)

