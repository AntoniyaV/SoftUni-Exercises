from project.card.card import Card


class MagicCard(Card):
    card_damage_points = 5
    card_health_points = 80

    def __init__(self, name):
        super().__init__(name, self.card_damage_points, self.card_health_points)
