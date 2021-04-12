from project.medicine.medicine import Medicine
from project.survivor import Survivor


class Salve(Medicine):
    default_health_increase = 50

    def __init__(self):
        super().__init__(self.default_health_increase)

    def apply(self, survivor: Survivor):
        survivor.health += self.health_increase
