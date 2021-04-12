class Survivor:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.health = 100
        self.needs = 100
        self.needs_sustenance = False
        self.needs_healing = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name not valid!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age not valid!")
        self.__age = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Health not valid!")
        if value > 100:
            value = 100
        self.__health = value
        self.needs_healing = self.is_less_than_100(self.health)

    @property
    def needs(self):
        return self.__needs

    @needs.setter
    def needs(self, value):
        if value < 0:
            raise ValueError("Needs not valid!")
        if value > 100:
            value = 100
        self.__needs = value
        self.needs_sustenance = self.is_less_than_100(self.needs)

    @staticmethod
    def is_less_than_100(value):
        return value < 100
