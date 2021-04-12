from project.player.player import Player


class Beginner(Player):
    initial_health_points = 50

    def __init__(self, username):
        super().__init__(username, self.initial_health_points)

    def take_damage(self, damage_points: int):
        if damage_points < 0:
            raise ValueError("Damage points cannot be less than zero.")
        self.health -= damage_points
