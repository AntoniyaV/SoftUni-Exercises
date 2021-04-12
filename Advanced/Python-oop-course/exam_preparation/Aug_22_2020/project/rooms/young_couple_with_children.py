from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name, salary_one, salary_two, *children):
        super().__init__(family_name, salary_one+salary_two, members_count=2+len(children))
        self.room_cost = 30
        self.appliances = self.generate_appliances(self.members_count)
        self.children = list(children)
        self.calculate_expenses(self.appliances, self.children)

    @staticmethod
    def generate_appliances(count):
        appliances = []
        for _ in range(count):
            appliances += [TV(), Fridge(), Laptop()]
        return appliances
