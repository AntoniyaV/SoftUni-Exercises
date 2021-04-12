from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    @staticmethod
    def get_player(name, players):
        return [player for player in players if player.username == name]

    def add(self, player: Player):
        if self.get_player(player.username, self.players):
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        if player == "":
            raise ValueError("Player cannot be an empty string!")
        player_instance = self.get_player(player, self.players)[0]
        index = self.players.index(player_instance)
        self.players.pop(index)
        self.count -= 1

    def find(self, username: str):
        return self.get_player(username, self.players)[0]
