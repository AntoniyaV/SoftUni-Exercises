from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    aquarium_types = ["FreshwaterAquarium", "SaltwaterAquarium"]
    decoration_types = ["Ornament", "Plant"]
    fish_types = ["FreshwaterFish", "SaltwaterFish"]

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    @staticmethod
    def is_type_valid(given_type, valid_types):
        return given_type in valid_types

    @staticmethod
    def create_aquarium(aq_type, aq_name):
        if aq_type == "FreshwaterAquarium":
            return FreshwaterAquarium(aq_name)
        if aq_type == "SaltwaterAquarium":
            return SaltwaterAquarium(aq_name)

    @staticmethod
    def create_decoration(dec_type):
        if dec_type == "Ornament":
            return Ornament()
        if dec_type == "Plant":
            return Plant()

    @staticmethod
    def create_fish(fish_type, name, species, price):
        if fish_type == "FreshwaterFish":
            return FreshwaterFish(name, species, price)
        if fish_type == "SaltwaterFish":
            return SaltwaterFish(name, species, price)

    @staticmethod
    def get_decoration(dec_type, repository):
        decoration = repository.find_by_type(dec_type)
        return None if decoration == "None" else decoration

    @staticmethod
    def get_aquarium(name, aquariums):
        match = [aqua for aqua in aquariums if aqua.name == name]
        return None if not match else match[0]

    @staticmethod
    def get_total_price(elements):
        return sum([el.price for el in elements])

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if not self.is_type_valid(aquarium_type, self.aquarium_types):
            return "Invalid aquarium type."

        aquarium = self.create_aquarium(aquarium_type, aquarium_name)
        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if not self.is_type_valid(decoration_type, self.decoration_types):
            return "Invalid decoration type."

        decoration = self.create_decoration(decoration_type)
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.get_decoration(decoration_type, self.decorations_repository)
        aquarium = self.get_aquarium(aquarium_name, self.aquariums)
        if not decoration:
            return f"There isn't a decoration of type {decoration_type}."

        if decoration and aquarium:
            aquarium.decorations.append(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if not self.is_type_valid(fish_type, self.fish_types):
            return f"There isn't a fish of type {fish_type}."

        fish = self.create_fish(fish_type, fish_name, fish_species, price)
        aquarium = self.get_aquarium(aquarium_name, self.aquariums)
        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = self.get_aquarium(aquarium_name, self.aquariums)
        aquarium.feed()
        fed_count = len(aquarium.fish)
        return f"Fish fed: {fed_count}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.get_aquarium(aquarium_name, self.aquariums)
        fish_prices = self.get_total_price(aquarium.fish)
        decorations_prices = self.get_total_price(aquarium.decorations)
        value = fish_prices + decorations_prices
        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        result = []
        for aquarium in self.aquariums:
            result.append(str(aquarium))

        return '\n'.join(result)
