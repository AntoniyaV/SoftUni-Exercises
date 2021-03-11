class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.__name = name
        self.__dough = dough
        self.__toppings_capacity = toppings_capacity
        self.__toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        self.__toppings_capacity = value

    @property
    def toppings(self):
        return self.__toppings

    @toppings.setter
    def toppings(self, value):
        pass

    @staticmethod
    def is_enough_capacity(num_toppings, capacity):
        return num_toppings < capacity

    @staticmethod
    def get_toppings_weight(toppings):
        return sum([value for value in toppings.values()])

    def add_topping(self, topping):
        if not self.is_enough_capacity(len(self.__toppings), self.__toppings_capacity):
            raise ValueError("Not enough space for another topping")

        if topping.topping_type not in self.__toppings:
            self.__toppings[topping.topping_type] = 0
        self.__toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self):
        total_weight = self.get_toppings_weight(self.__toppings) + self.__dough.weight
        return total_weight
