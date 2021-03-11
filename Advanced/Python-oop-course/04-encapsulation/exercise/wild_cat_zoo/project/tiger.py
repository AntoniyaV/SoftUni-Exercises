class Tiger:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self.__needs = 45

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

    def get_needs(self):
        return self.__needs
