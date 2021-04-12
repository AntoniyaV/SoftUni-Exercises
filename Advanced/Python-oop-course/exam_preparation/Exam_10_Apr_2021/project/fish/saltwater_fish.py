from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    initial_size = 5
    default_size_increase = 2

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.initial_size, price)
