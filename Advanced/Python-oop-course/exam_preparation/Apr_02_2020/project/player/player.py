from abc import ABC, abstractmethod
from project.card.card_repository import CardRepository


class Player(ABC):
    def __init__(self, username: str, health: int):
        self.username = username
        self.health = health
        self.card_repository = CardRepository()
        self.is_dead = False

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value == "":
            raise ValueError("Player's username cannot be an empty string.")
        self.__username = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Player's health bonus cannot be less than zero.")
        self.__health = value
        self.is_dead = self.value_is_0_or_less(self.health)

    @staticmethod
    def value_is_0_or_less(value):
        return value <= 0

    @abstractmethod
    def take_damage(self, damage_points: int):
        pass
