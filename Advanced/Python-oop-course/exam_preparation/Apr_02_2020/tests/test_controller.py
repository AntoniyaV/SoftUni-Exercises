import unittest
from project.controller import Controller


class ControllerTests(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()

    def test_init__expect_attributes_to_be_set(self):
        self.assertEqual([], self.controller.player_repository.players)
        self.assertEqual(0, self.controller.player_repository.count)
        self.assertEqual([], self.controller.card_repository.cards)
        self.assertEqual(0, self.controller.card_repository.count)

    def test_add_player__expect_to_create_and_add_player_of_given_type_and_name_and_return_msg(self):
        expected_msg = "Successfully added player of type Advanced with username: frodo"
        actual_msg = self.controller.add_player("Advanced", "frodo")

        self.assertEqual(1, self.controller.player_repository.count)
        self.assertEqual(expected_msg, actual_msg)

    def test_add_card__expect_to_create_and_add_card_of_given_type_and_name_and_return_msg(self):
        expected_msg = "Successfully added card of type MagicCard with name: magic"
        actual_msg = self.controller.add_card("Magic", "magic")

        self.assertEqual(1, self.controller.card_repository.count)
        self.assertEqual(expected_msg, actual_msg)

    def test_add_player_card__expect_to_add_card_object_to_player_object(self):
        self.controller.add_player("Advanced", "frodo")
        self.controller.add_card("Magic", "magic")
        expected_msg = "Successfully added card: magic to user: frodo"
        actual_msg = self.controller.add_player_card("frodo", "magic")

        self.assertEqual(1, self.controller.player_repository.players[0].card_repository.count)
        self.assertEqual(expected_msg, actual_msg)

    def test_fight(self):
        self.controller.add_player("Advanced", "Aragorn")
        self.controller.add_card("Trap", "sword")
        self.controller.add_player_card("Aragorn", "sword")

        self.controller.add_player("Beginner", "Orc")
        self.controller.add_card("Trap", "axe")
        self.controller.add_player_card("Orc", "axe")

        expected_msg = "Attack user health 255 - Enemy user health 0"
        actual_msg = self.controller.fight("Aragorn", "Orc")
        self.assertEqual(expected_msg, actual_msg)

    def test_report__expect_info_for_players_and_their_cards_as_string(self):
        self.controller.add_player("Advanced", "frodo")
        self.controller.add_card("Magic", "magic")
        self.controller.add_player_card("frodo", "magic")

        self.controller.add_player("Beginner", "sam")
        self.controller.add_card("Trap", "trap")
        self.controller.add_player_card("sam", "trap")

        expected_msg = "Username: frodo - Health: 250 - Cards 1\n### Card: magic - Damage: 5\n" \
                       "Username: sam - Health: 50 - Cards 1\n### Card: trap - Damage: 120"
        actual_msg = self.controller.report()
        self.assertEqual(expected_msg, actual_msg)


if __name__ == "__main__":
    unittest.main()