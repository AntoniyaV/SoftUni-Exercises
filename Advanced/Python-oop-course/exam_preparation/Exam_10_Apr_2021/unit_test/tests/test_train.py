import unittest
from project.train.train import Train


class TrainTests(unittest.TestCase):
    def setUp(self):
        self.train = Train("Orient", 50)

    def test_init__expect_attributes_to_be_set(self):
        self.assertEqual("Orient", self.train.name)
        self.assertEqual(50, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_class_attributes__expect_to_be_set(self):
        self.assertEqual("Train is full", self.train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", self.train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", self.train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", self.train.PASSENGER_ADD)
        self.assertEqual("Removed {}", self.train.PASSENGER_REMOVED)
        self.assertEqual(0, self.train.ZERO_CAPACITY)

    def test_add__expect_to_add_passenger_and_return_msg(self):
        expected_message = "Added passenger john"
        actual_message = self.train.add("john")
        self.assertEqual(expected_message, actual_message)
        self.assertEqual(["john"], self.train.passengers)

    def test_add__when_capacity_is_full_expect_value_error(self):
        self.train.capacity = 0
        with self.assertRaises(ValueError) as err:
            self.train.add("john")
        self.assertEqual("Train is full", str(err.exception))

    def test_add__when_passenger_already_in_passengers_expect_value_error(self):
        self.train.add("john")
        with self.assertRaises(ValueError) as err:
            self.train.add("john")
        self.assertEqual("Passenger john Exists", str(err.exception))

    def test_remove__expect_to_remove_passenger_and_return_msg(self):
        self.train.add("john")
        expected_message = "Removed john"
        actual_message = self.train.remove("john")
        self.assertEqual(expected_message, actual_message)
        self.assertEqual([], self.train.passengers)

    def test_remove__when_passenger_not_in_passengers__expect_value_error(self):
        with self.assertRaises(ValueError) as err:
            self.train.remove("john")
        self.assertEqual("Passenger Not Found", str(err.exception))


if __name__ == "__main__":
    unittest.main()
