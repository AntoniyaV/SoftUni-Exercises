from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    initial_capacity = 25
    fish_types = ["SaltwaterFish"]

    def __init__(self, name: str):
        super().__init__(name, self.initial_capacity)
