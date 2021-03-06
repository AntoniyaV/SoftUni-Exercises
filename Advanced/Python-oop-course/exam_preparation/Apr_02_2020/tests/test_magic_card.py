import unittest
from project.card.magic_card import MagicCard


class MagicCardTests(unittest.TestCase):
    def setUp(self):
        self.card = MagicCard("magic")

    def test_init__expect_attributes_to_be_set(self):
        self.assertEqual("magic", self.card.name)
        self.assertEqual(5, self.card.damage_points)
        self.assertEqual(80, self.card.health_points)

    def test_name__when_set_as_empty_string_expect_value_error(self):
        with self.assertRaises(ValueError) as err:
            self.card.name = ""
        self.assertEqual("Card's name cannot be an empty string.", str(err.exception))

    def test_damage_points__when_set_to_less_than_0_expect_value_error(self):
        with self.assertRaises(ValueError) as err:
            self.card.damage_points = -10
        self.assertEqual("Card's damage points cannot be less than zero.", str(err.exception))

    def test_health_points__when_set_to_less_than_0_expect_value_error(self):
        with self.assertRaises(ValueError) as err:
            self.card.health_points = -10
        self.assertEqual("Card's HP cannot be less than zero.", str(err.exception))


if __name__ == "__main__":
    unittest.main()
