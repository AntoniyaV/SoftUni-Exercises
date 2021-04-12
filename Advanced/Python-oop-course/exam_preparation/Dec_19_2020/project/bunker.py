from project.medicine.medicine import Medicine
from project.medicine.painkiller import Painkiller
from project.medicine.salve import Salve
from project.supply.food_supply import FoodSupply
from project.supply.supply import Supply
from project.supply.water_supply import WaterSupply
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food = [supply for supply in self.supplies if isinstance(supply, FoodSupply)]
        if not food:
            raise IndexError("There are no food supplies left!")
        return food

    @property
    def water(self):
        water = [supply for supply in self.supplies if isinstance(supply, WaterSupply)]
        if not water:
            raise IndexError("There are no water supplies left!")
        return water

    @property
    def painkillers(self):
        painkillers = [medicine for medicine in self.medicine if isinstance(medicine, Painkiller)]
        if not painkillers:
            raise IndexError("There are no painkillers left!")
        return painkillers

    @property
    def salves(self):
        salves = [medicine for medicine in self.medicine if isinstance(medicine, Salve)]
        if not salves:
            raise IndexError("There are no salves left!")
        return salves

    def get_element(self, el_type):
        if el_type == "FoodSupply":
            return self.food.pop()
        if el_type == "WaterSupply":
            return self.water.pop()
        if el_type == "Painkiller":
            return self.painkillers.pop()
        if el_type == "Salve":
            return self.salves.pop()

    def add_survivor(self, survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        if survivor.needs_healing:
            medicine = self.get_element(medicine_type)
            medicine.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            supply = self.get_element(sustenance_type)
            supply.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            reduction = survivor.age * 2
            survivor.needs -= reduction
            self.sustain(survivor, "FoodSupply")
            self.sustain(survivor, "WaterSupply")
