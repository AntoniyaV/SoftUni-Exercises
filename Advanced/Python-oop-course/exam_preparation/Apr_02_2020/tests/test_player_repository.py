import unittest
from project.player.player_repository import PlayerRepository
from project.player.beginner import Beginner


class PlayerRepositoryTests(unittest.TestCase):
    def setUp(self):
        self.repository = PlayerRepository()

    def test_init__expect_attributes_to_be_set(self):
        self.assertEqual(0, self.repository.count)
        self.assertEqual([], self.repository.players)

    def test_add__when_player_not_in_players_expect_to_add_player(self):
        player = Beginner("sam")
        self.repository.add(player)
        self.assertEqual([player], self.repository.players)
        self.assertEqual(1, self.repository.count)

    def test_add__when_player_exists_expect_value_error(self):
        player = Beginner("sam")
        self.repository.add(player)
        with self.assertRaises(ValueError) as err:
            self.repository.add(player)
        self.assertEqual("Player sam already exists!", str(err.exception))

    def test_remove__when_player_is_empty_string_expect_value_error(self):
        with self.assertRaises(ValueError) as err:
            self.repository.remove("")
        self.assertEqual("Player cannot be an empty string!", str(err.exception))

    def test_remove_player__expect_to_remove_player(self):
        player = Beginner("sam")
        self.repository.add(player)

        self.repository.remove("sam")
        self.assertEqual([], self.repository.players)
        self.assertEqual(0, self.repository.count)

    def test_find__expect_to_return_object_player_with_given_name(self):
        player = Beginner("sam")
        self.repository.add(player)

        actual = self.repository.find("sam")
        self.assertEqual(player, actual)


if __name__ == "__main__":
    unittest.main()