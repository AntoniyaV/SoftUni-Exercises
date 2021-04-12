from exercise.hero.project.hero import Hero
import unittest


class HeroTests(unittest.TestCase):
    username = "steve"
    level = 5
    health = 70
    damage = 5

    def setUp(self):
        self.hero = Hero(self.username, self.level, self.health, self.damage)

    def test_hero_init__expect_parameteres_to_be_set(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_hero_battle__when_both_heroes_have_same_username_expect_exception(self):
        enemy_hero = self.hero
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)
        expected_msg = "You cannot fight yourself"
        actual_msg = str(ex.exception)
        self.assertEqual(expected_msg, actual_msg)

    def test_hero_battle__when_hero_health_is_below_or_equal_to_0_expect_value_error(self):
        self.hero.health = 0
        enemy_hero = Hero("alan", 3, 65, 3)
        with self.assertRaises(ValueError) as err:
            self.hero.battle(enemy_hero)
        expected_msg = "Your health is lower than or equal to 0. You need to rest"
        actual_msg = str(err.exception)
        self.assertEqual(expected_msg, actual_msg)

    def test_hero_battle__when_enemy_health_is_below_or_equal_to_0_expect_value_error(self):
        enemy_hero = Hero("alan", 3, 0, 3)
        with self.assertRaises(ValueError) as err:
            self.hero.battle(enemy_hero)
        expected_msg = f"You cannot fight {enemy_hero.username}. He needs to rest"
        actual_msg = str(err.exception)
        self.assertEqual(expected_msg, actual_msg)

    def test_hero_battle__when_after_damage_both_heroes_health_is_below_or_equal_to_zero_expect_draw(self):
        enemy_hero = Hero("alan", 3, 20, 3)
        self.hero.health = 9
        expected = "Draw"
        actual = self.hero.battle(enemy_hero)
        self.assertEqual(expected, actual)

    def test_hero_battle__when_after_damage_enemy_health_is_below_or_equal_to_zero_expect_to_win(self):
        enemy_hero = Hero("alan", 3, 20, 3)
        expected = "You win"
        actual = self.hero.battle(enemy_hero)
        self.assertEqual(expected, actual)

    def test_hero_battle__when_hero_wins_expect_his_level_health_and_damage_to_increment(self):
        enemy_hero = Hero("alan", 3, 20, 3)
        self.hero.battle(enemy_hero)
        self.assertEqual(self.level + 1, self.hero.level)
        self.assertEqual(self.health - 9 + 5, self.hero.health)
        self.assertEqual(self.damage + 5, self.hero.damage)

    def test_hero_battle__when_after_damage_enemy_health_is_above_zero_expect_to_lose(self):
        enemy_hero = Hero("alan", 40, 75, 4)
        expected = "You lose"
        actual = self.hero.battle(enemy_hero)
        self.assertEqual(expected, actual)

    def test_hero_battle__when_enemy_wins_expect_his_level_health_and_damage_to_increment(self):
        enemy_hero = Hero("alan", 40, 75, 4)
        self.hero.battle(enemy_hero)
        self.assertEqual(41, enemy_hero.level)
        self.assertEqual(55, enemy_hero.health)
        self.assertEqual(9, enemy_hero.damage)

    def test_hero_str_representation_expect_correct_format(self):
        expected = f"Hero {self.username}: {self.level} lvl\nHealth: {self.health}\nDamage: {self.damage}\n"
        actual = str(self.hero)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
