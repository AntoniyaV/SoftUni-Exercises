import unittest
from project.rooms.room import Room
from project.people.child import Child
from project.appliances.tv import TV
from project.appliances.laptop import Laptop
from project.appliances.stove import Stove
from project.appliances.fridge import Fridge


class RoomTests(unittest.TestCase):
    def setUp(self):
        self.room = Room("Smith", 1000, 3)

    def test_room_init_expect_attributes_to_be_set(self):
        self.assertEqual("Smith", self.room.family_name)
        self.assertEqual(1000, self.room.budget)
        self.assertEqual(3, self.room.members_count)
        self.assertEqual([], self.room.children)
        self.assertEqual(0, self.room.expenses)

    def test_room_expenses_setter__when_value_is_less_than_zero_expect_value_error(self):
        with self.assertRaises(ValueError) as err:
            self.room.expenses = -20
        self.assertEqual("Expenses cannot be negative", str(err.exception))

    def test_room_calculate_expenses__expect_calculation_of_all_costs_for_one_month(self):
        self.room.children = [Child(5, 5, 5), Child(4, 6, 2)]
        appliances = [Fridge(), Laptop(), Stove(), TV()]
        self.room.calculate_expenses(self.room.children, appliances)

        expected_cost = 942
        actual_cost = self.room.expenses
        self.assertEqual(expected_cost, actual_cost)


if __name__ == "__main__":
    unittest.main()
