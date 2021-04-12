from project.vehicle import Vehicle
import unittest


class VehicleTests(unittest.TestCase):
    fuel = 50
    capacity = fuel
    horse_power = 20
    fuel_consumption = 1.25

    def setUp(self):
        self.car = Vehicle(self.fuel, self.horse_power)

    def test_vehicle_init__expect_parameters_to_be_set(self):
        self.assertEqual(self.fuel, self.car.fuel)
        self.assertEqual(self.capacity, self.car.capacity)
        self.assertEqual(self.horse_power, self.car.horse_power)
        self.assertEqual(self.fuel_consumption, self.car.fuel_consumption)

    def test_vehicle_drive__when_needed_fuel_exceeds_fuel_expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(50)
        expected_message = "Not enough fuel"
        actual_message = str(ex.exception)
        self.assertEqual(expected_message, actual_message)

    def test_vehicle_drive__when_needed_fuel_does_not_exceed_fuel_expect_fuel_to_decrease_with_nedded_fuel(self):
        self.car.drive(30)
        expected_fuel = 12.5
        actual_fuel = self.car.fuel
        self.assertEqual(expected_fuel, actual_fuel)

    def test_vehicle_refuel__when_added_fuel_and_fuel_exceed_capacity_expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(10)
        expected_message = "Too much fuel"
        actual_message = str(ex.exception)
        self.assertEqual(expected_message, actual_message)

    def test_vehicle_refuel__when_added_fuel_and_fuel_do_not_exceed_capacity_expect_fuel_to_increase_with_added_fuel(self):
        self.car.fuel = 20
        self.car.refuel(10)
        expected_fuel = 30
        actual_fuel = self.car.fuel
        self.assertEqual(expected_fuel, actual_fuel)

    def test_vehicle_str__expect_string_representation_in_correct_format(self):
        expected = f"The vehicle has {self.horse_power} " \
                   f"horse power with {self.fuel} fuel left and {self.fuel_consumption} fuel consumption"
        actual = str(self.car)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
