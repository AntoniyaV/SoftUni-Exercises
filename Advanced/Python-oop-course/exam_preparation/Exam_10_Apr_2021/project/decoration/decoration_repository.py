from project.decoration.base_decoration import BaseDecoration
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant


class DecorationRepository:
    def __init__(self):
        self.decorations = []

    @staticmethod
    def get_decoration(decoration_type, decorations):
        for decor in decorations:
            if decoration_type == "Plant" and isinstance(decor, Plant):
                return decor
            if decoration_type == "Ornament" and isinstance(decor, Ornament):
                return decor
        return "None"

    def add(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def remove(self, decoration: BaseDecoration):
        if decoration not in self.decorations:
            return False

        index = self.decorations.index(decoration)
        self.decorations.pop(index)
        return True

    def find_by_type(self, decoration_type: str):
        decoration = self.get_decoration(decoration_type, self.decorations)
        return decoration
