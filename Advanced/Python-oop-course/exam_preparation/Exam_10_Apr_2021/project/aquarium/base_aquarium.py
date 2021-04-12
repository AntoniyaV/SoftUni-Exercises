from abc import ABC, abstractmethod
from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):
    fish_types = ["FreshwaterFish", "SaltwaterFish"]

    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    @staticmethod
    def is_capacity_enough(capacity, num_fish):
        return capacity > num_fish

    @staticmethod
    def get_fish_names(fish):
        names = [f.name for f in fish]
        return ' '.join(names) if names else "none"

    def calculate_comfort(self):
        total_comfort = sum([decoration.comfort for decoration in self.decorations])
        return total_comfort

    def add_fish(self, fish: BaseFish):
        if not self.is_capacity_enough(self.capacity, len(self.fish)):
            return "Not enough capacity."

        fish_type = fish.__class__.__name__
        if fish_type not in self.fish_types:
            return "Water not suitable."

        self.fish.append(fish)
        return f"Successfully added {fish_type} to {self.name}."

    def remove_fish(self, fish: BaseFish):
        self.fish.remove(fish)

    def add_decoration(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        names = self.get_fish_names(self.fish)
        comfort = self.calculate_comfort()
        result = f"{self.name}:\nFish: {names}\nDecorations: {len(self.decorations)}\nComfort: {comfort}"
        return result
