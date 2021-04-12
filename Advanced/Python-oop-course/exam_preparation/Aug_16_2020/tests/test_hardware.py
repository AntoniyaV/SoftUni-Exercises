from project.hardware.hardware import Hardware
from project.software.software import Software
import unittest


class HardwareTests(unittest.TestCase):
    def setUp(self):
        self.hardware = Hardware("HDD", "Heavy", 200, 200)

    def test_hardware_init__expect_attributes_to_be_set(self):
        self.assertEqual("HDD", self.hardware.name)
        self.assertEqual("Heavy", self.hardware.type)
        self.assertEqual(200, self.hardware.capacity)
        self.assertEqual(200, self.hardware.memory)
        self.assertEqual([], self.hardware.software_components)

    def test_hardware_install_software__when_capacity_is_not_enough_expect_exception(self):
        software = Software("Windows", "Light", 500, 10)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(software)
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_hardware_install_software__when_memory_is_not_enough_expect_exception(self):
        software = Software("Windows", "Light", 50, 1000)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(software)
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_hardware_install_software__when_capacity_and_memory_are_not_enough_expect_exception(self):
        software = Software("Windows", "Light", 500, 1000)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(software)
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_hardware_install_software__when_possible_expect_to_add_software(self):
        software = Software("Windows", "Light", 50, 10)
        self.hardware.install(software)
        self.assertEqual(1, len(self.hardware.software_components))

    def test_hardware_install_software__when_possible_expect_to_decrease_hardware_memory_and_capacity(self):
        software = Software("Windows", "Light", 50, 10)
        self.hardware.install(software)

        expected_capacity = 150
        expected_memory = 190
        self.assertEqual(expected_capacity, self.hardware.capacity)
        self.assertEqual(expected_memory, self.hardware.memory)

    def test_hardware_uninstall__expect_to_remove_software(self):
        software = Software("Windows", "Light", 50, 10)
        self.hardware.install(software)
        self.hardware.uninstall(software)
        self.assertEqual(0, len(self.hardware.software_components))

    def test_hardware_uninstall__expect_to_increase_hardware_memory_and_capacity(self):
        software = Software("Windows", "Light", 50, 10)
        self.hardware.install(software)
        self.hardware.uninstall(software)

        expected_capacity = 200
        expected_memory = 200
        self.assertEqual(expected_capacity, self.hardware.capacity)
        self.assertEqual(expected_memory, self.hardware.memory)


if __name__ == "__main__":
    unittest.main()
