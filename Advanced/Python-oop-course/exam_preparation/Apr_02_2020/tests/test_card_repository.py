import unittest
from project.card.card_repository import CardRepository
from project.card.trap_card import TrapCard


class CardRepositoryTests(unittest.TestCase):
    def setUp(self):
        self.repository = CardRepository()

    def test_init__expect_attributes_to_be_set(self):
        self.assertEqual(0, self.repository.count)
        self.assertEqual([], self.repository.cards)

    def test_add__when_card_not_in_cards_expect_to_add_card(self):
        card = TrapCard("trap")
        self.repository.add(card)
        self.assertEqual([card], self.repository.cards)
        self.assertEqual(1, self.repository.count)

    def test_add__when_card_exists_expect_value_error(self):
        card = TrapCard("trap")
        self.repository.add(card)
        with self.assertRaises(ValueError) as err:
            self.repository.add(card)
        self.assertEqual("Card trap already exists!", str(err.exception))

    def test_remove__when_card_is_empty_string_expect_value_error(self):
        with self.assertRaises(ValueError) as err:
            self.repository.remove("")
        self.assertEqual("Card cannot be an empty string!", str(err.exception))

    def test_remove_card__expect_to_remove_card(self):
        card = TrapCard("trap")
        self.repository.add(card)

        self.repository.remove("trap")
        self.assertEqual([], self.repository.cards)
        self.assertEqual(0, self.repository.count)

    def test_find__expect_to_return_object_card_with_given_name(self):
        card = TrapCard("trap")
        self.repository.add(card)

        actual = self.repository.find("trap")
        self.assertEqual(card, actual)


if __name__ == "__main__":
    unittest.main()