from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    @staticmethod
    def get_card(name, cards):
        return [card for card in cards if card.name == name]

    def add(self, card: Card):
        if self.get_card(card.name, self.cards):
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        card_instance = self.get_card(card, self.cards)[0]
        index = self.cards.index(card_instance)
        self.cards.pop(index)
        self.count -= 1

    def find(self, name: str):
        return self.get_card(name, self.cards)[0]
