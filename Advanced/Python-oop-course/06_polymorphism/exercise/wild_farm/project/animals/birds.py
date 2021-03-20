from project.animals.animal import Bird


class Owl(Bird):
    foods = {"Meat"}
    weight_increase = 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    foods = {"Vegetable", "Fruit", "Meat", "Seed"}
    weight_increase = 0.35

    def make_sound(self):
        return "Cluck"
