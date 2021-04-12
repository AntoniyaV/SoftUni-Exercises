from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop


class YoungCouple(Room):
    def __init__(self, family_name, salary_one, salary_two):
        super().__init__(family_name, salary_one+salary_two, members_count=2)
        self.room_cost = 20
        self.appliances = [TV(), Fridge(), Laptop(), TV(), Fridge(), Laptop()]
        self.calculate_expenses(self.appliances)
