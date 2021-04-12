from project.card.card import Card


class TrapCard(Card):
    card_damage_points = 120
    card_health_points = 5

    def __init__(self, name):
        super().__init__(name, self.card_damage_points, self.card_health_points)
