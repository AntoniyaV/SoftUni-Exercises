from project.car_manager import Car
import unittest


class CarManagerTests(unittest.TestCase):
    make = "BMW"
    model = 6
    fuel_consumption = 3
    fuel_capacity = 50

    def setUp(self):
        self.car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)

    def test_car_make_getter__expect_correct_value(self):
        self.assertEqual(self.make, self.car.make)

    def test_car_make_setter__when_value_is_none_or_null_expect_exception(self):
        with self.assertRaises(Exception):
            self.car.make = None

    def test_car_make_setter__when_value_is_valid_expect_make_to_be_changed_with_the_value(self):
        self.car.make = "Ford"
        expected = "Ford"
        actual = self.car.make
        self.assertEqual(expected, actual)

    def test_car_model_getter__expect_correct_value(self):
        self.assertEqual(self.model, self.car.model)

    def test_car_model_setter__when_value_is_none_or_null_expect_exception(self):
        with self.assertRaises(Exception):
            self.car.model = None

    def test_car_model_setter__when_value_is_valid_expect_model_to_be_changed_with_the_value(self):
        self.car.make = "GT"
        expected = "GT"
        actual = self.car.make
        self.assertEqual(expected, actual)

    def test_car_fuel_consumption_getter__expect_correct_value(self):
        self.assertEqual(self.fuel_consumption, self.car.fuel_consumption)

    def test_car_fuel_consumption_setter__when_value_is_0_expect_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_consumption = 0

    def test_car_fuel_consumption_setter__when_value_is_negative_expect_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_consumption= -2

    def test_car_fuel_consumption_setter__when_value_is_valid_expect_fuel_consumption_to_be_changed_with_the_value(self):
        self.car.fuel_consumption = 2
        expected = 2
        actual = self.car.fuel_consumption
        self.assertEqual(expected, actual)

    def test_car_fuel_capacity_getter__expect_correct_value(self):
        self.assertEqual(self.fuel_capacity, self.car.fuel_capacity)

    def test_car_fuel_capacity_setter__when_value_is_0_expect_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_capacity = 0

    def test_car_fuel_capacity_setter__when_value_is_negative_expect_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_capacity = -20

    def test_car_fuel_capacity_setter__when_value_is_valid_expect_fuel_capacity_to_be_changed_with_the_value(self):
        self.car.fuel_capacity = 20
        expected = 20
        actual = self.car.fuel_capacity
        self.assertEqual(expected, actual)

    def test_car_fuel_amount_getter__expect_correct_value(self):
        self.assertEqual(0, self.car.fuel_amount)

    def test_car_fuel_amount_setter__when_value_is_negative_expect_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_amount = -20

    def test_car_fuel_amount_setter__when_value_is_valid_expect_fuel_amount_to_be_changed_with_the_value(self):
        self.car.fuel_amount = 20
        expected = 20
        actual = self.car.fuel_amount
        self.assertEqual(expected, actual)

    def test_car_refuel__when_fuel_value_is_0_expect_exception(self):
        with self.assertRaises(Exception):
            self.car.refuel(0)

    def test_car_refuel__when_fuel_value_is_negative_expect_exception(self):
        with self.assertRaises(Exception):
            self.car.refuel(-10)

    def test_car_refuel__when_fuel_value_is_positive_expect_fuel_amount_to_increase_with_fuel_value(self):
        self.car.refuel(10)
        expected = 10
        actual = self.car.fuel_amount
        self.assertEqual(expected, actual)

    def test_car_refuel__when_fuel_amount_is_greater_than_fuel_capacity_expect_fuel_amount_to_be_equal_to_fuel_capacity(self):
        self.car.refuel(60)
        expected = self.fuel_capacity
        actual = self.car.fuel_amount
        self.assertEqual(expected, actual)

    def test_car_drive__when_needed_fuel_is_greater_than_fuel_amount_expect_exception(self):
        with self.assertRaises(Exception):
            self.car.drive(10)

    def test_car_drive__when_needed_fuel_is_less_than_or_equal_to_fuel_amount_expect_fuel_amount_to_decrease_with_needed_fuel(self):
        self.car.refuel(50)
        self.car.drive(1000)
        expected = 20
        actual = self.car.fuel_amount
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
