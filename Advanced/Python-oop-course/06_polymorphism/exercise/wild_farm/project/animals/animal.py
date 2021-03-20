from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name, weight, food_eaten=0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass


class Bird(Animal):
    foods = set()
    weight_increase = 0

    def __init__(self, name, weight, wing_size, food_eaten=0):
        super().__init__(name, weight, food_eaten=0)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"

    def make_sound(self):
        pass

    def feed(self, food):
        food_type = food.__class__.__name__
        if food_type not in self.foods:
            return f"{self.__class__.__name__} does not eat {food_type}!"

        self.weight += food.quantity * self.weight_increase
        self.food_eaten += food.quantity


class Mammal(Animal):
    foods = set()
    weight_increase = 0

    def __init__(self, name, weight, living_region, food_eaten=0):
        super().__init__(name, weight, food_eaten=0)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

    def make_sound(self):
        pass

    def feed(self, food):
        food_type = food.__class__.__name__
        if food_type not in self.foods:
            return f"{self.__class__.__name__} does not eat {food_type}!"

        self.weight += food.quantity * self.weight_increase
        self.food_eaten += food.quantity
