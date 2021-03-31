from project.cat import Cat
import unittest


class CatTests(unittest.TestCase):
    name = "Jeff"

    def setUp(self):
        self.cat = Cat(self.name)

    def test_cat_eat__expect_size_to_be_incremented(self):
        self.cat.eat()
        expected_size = 1
        self.assertEqual(expected_size, self.cat.size)

    def test_cat_eat__expect_fed_to_be_true(self):
        self.cat.eat()
        expected = True
        self.assertEqual(expected, self.cat.fed)

    def test_cat_eat__when_already_fed_expect_exception(self):
        self.cat.eat()
        with self.assertRaises(Exception):
            self.cat.eat()

    def test_cat_sleep__when_not_fed_expect_exception(self):
        with self.assertRaises(Exception):
            self.cat.sleep()

    def test_cat_sleep__when_fed_expect_sleepy_to_be_false(self):
        self.cat.eat()
        self.cat.sleep()
        expected = False
        self.assertEqual(expected, self.cat.sleepy)


if __name__ == "__main__":
    unittest.main()