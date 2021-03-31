import unittest
from project.worker import Worker


class WorkerTests(unittest.TestCase):
    name = "John"
    salary = 1200
    energy = 5

    def setUp(self):
        self.worker = Worker(self.name, self.salary, self.energy)

    def test_worker_init__expect_proper_initialization(self):
        self.assertEqual(self.name, self.worker.name)
        self.assertEqual(self.salary, self.worker.salary)
        self.assertEqual(self.energy, self.worker.energy)

    def test_worker_rest__expect_energy_to_be_incremented_with_1(self):
        self.worker.rest()
        expected_energy = self.energy + 1
        self.assertEqual(expected_energy, self.worker.energy)

    def test_worker_work__when_energy_is_zero_expect_to_raise_exception(self):
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_worker_work__when_energy_is_above_zero_expect_to_increase_money_with_salary(self):
        self.worker.work()
        expected_money = self.salary
        self.assertEqual(expected_money, self.worker.money)

    def test_worker_work__when_energy_is_above_zero_expect_to_decreases_energy_with_1(self):
        self.worker.work()
        expected_energy = self.energy - 1
        self.assertEqual(expected_energy, self.worker.energy)

    def test_worker_get_info__expect_correct_output_format(self):
        actual_result = self.worker.get_info()
        expected_result = f'{self.name} has saved 0 money.'
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
