from project.supply.supply import Supply
from project.survivor import Survivor


class WaterSupply(Supply):
    default_needs_increase = 40

    def __init__(self):
        super().__init__(self.default_needs_increase)

    def apply(self, survivor: Survivor):
        survivor.needs += self.needs_increase
