import unittest
from project.battle_field import BattleField
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class BattleFieldTests(unittest.TestCase):
    def setUp(self):
        self.battlefield = BattleField()

    def test_fight__when_at_least_one_player_is_dead_expect_value_error(self):
        attacker = Advanced("aragorn")
        enemy = Beginner("orc")
        enemy.is_dead = True
        with self.assertRaises(ValueError) as err:
            self.battlefield.fight(attacker, enemy)
        self.assertEqual("Player is dead!", str(err.exception))

    def test_fight__expect_players_health_and_card_damage_points_to_change(self):
        attacker = Advanced("aragorn")
        sword = TrapCard("sword")
        attacker.card_repository.add(sword)

        enemy = Beginner("orc")
        axe = TrapCard("axe")
        enemy.card_repository.add(axe)

        self.battlefield.fight(attacker, enemy)
        # before attack:
        # enemy health = 50 + 40; enemy card damage points = 120 + 30 --> beginner
        # enemy health = 90 + 5
        # attacker health = 250 + 5
        # after attack:
        # enemy health = 95 - 120 --> value error
        # attacker health = 255 - 150

        self.assertEqual(95, enemy.health)
        self.assertEqual(105, attacker.health)
        self.assertEqual(150, axe.damage_points)
        self.assertEqual(120, sword.damage_points)


if __name__ == "__main__":
    unittest.main()
