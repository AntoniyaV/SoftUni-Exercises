from project.player.beginner import Beginner
from project.player.player import Player


class BattleField:
    @staticmethod
    def increase_beginners_points(player):
        if isinstance(player, Beginner):
            player.health += 40
            for card in player.card_repository.cards:
                card.damage_points += 30
        return player

    @staticmethod
    def get_bonus_health(player):
        bonus_health = sum([card.health_points for card in player.card_repository.cards])
        player.health += bonus_health
        return player

    @staticmethod
    def opponent_is_dead(attacker, enemy):
        for card in attacker.card_repository.cards:
            try:
                enemy.take_damage(card.damage_points)
            except ValueError:
                enemy.is_dead = True
                enemy.health = 0
                break
        return True if enemy.is_dead else False

    def fight(self, attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        attacker = self.increase_beginners_points(attacker)
        enemy = self.increase_beginners_points(enemy)

        attacker = self.get_bonus_health(attacker)
        enemy = self.get_bonus_health(enemy)

        if not self.opponent_is_dead(attacker, enemy):
            self.opponent_is_dead(enemy, attacker)
