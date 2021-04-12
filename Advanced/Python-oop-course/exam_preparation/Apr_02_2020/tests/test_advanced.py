import unittest
from project.player.advanced import Advanced


class AdvancedTests(unittest.TestCase):
    def setUp(self):
        self.player = Advanced("henry")

    def test_init__expect_attributes_to_be_set(self):
        self.assertEqual("henry", self.player.username)
        self.assertEqual(250, self.player.health)
        self.assertEqual(False, self.player.is_dead)
        self.assertEqual([], self.player.card_repository.cards)
        self.assertEqual(0, self.player.card_repository.count)

    def test_username__when_set_to_empty_string_expect_value_error(self):
        with self.assertRaises(ValueError) as err:
            self.player.username = ""
        self.assertEqual("Player's username cannot be an empty string.", str(err.exception))

    def test_health__when_set_to_less_than_0_expect_value_error(self):
        with self.assertRaises(ValueError) as err:
            self.player.health = -50
        self.assertEqual("Player's health bonus cannot be less than zero.", str(err.exception))

    def test_take_damage__when_points_are_less_than_0_expect_value_error(self):
        with self.assertRaises(ValueError) as err:
            self.player.take_damage(-50)
        self.assertEqual("Damage points cannot be less than zero.", str(err.exception))

    def test_take_damage__when_health_gets_less_than_0_expect_value_error(self):
        with self.assertRaises(ValueError) as err:
            self.player.take_damage(300)
        self.assertEqual("Player's health bonus cannot be less than zero.", str(err.exception))

    # def test_take_damage__when_health_gets_less_than_0_expect_player_to_be_dead_and_health_0(self):
    #     with self.assertRaises(ValueError) as err:
    #         self.player.take_damage(300)
    #     self.assertEqual(True, self.player.is_dead)
    #     self.assertEqual(0, self.player.health)

    def test_take_damage__when_health_is_0_expect_player_to_be_dead_and_health_0(self):
        self.player.take_damage(250)
        self.assertEqual(True, self.player.is_dead)
        self.assertEqual(0, self.player.health)

    def test_take_damage__expect_health_to_decrease_with_given_points_and_not_to_be_dead(self):
        self.player.take_damage(100)
        self.assertEqual(150, self.player.health)
        self.assertEqual(False, self.player.is_dead)


if __name__ == "__main__":
    unittest.main()